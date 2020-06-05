from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview import RecycleView
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import (
    BooleanProperty, StringProperty,
     NumericProperty, ObjectProperty
    )
from kivy.lang import Builder

Builder.load_string("""

<A>:
    canvas.before:
        Color:
            rgba: (1, 1, 1, 1)
        Rectangle:
            pos: self.pos
            size: self.size

<B>:
    orientation: 'vertical'

""")

class HoverBehavior(object):

    hovered = BooleanProperty(False)
    border_point= ObjectProperty(None)

    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return 
        pos = args[1]
        
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
           
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass

class A(ButtonBehavior, BoxLayout ,HoverBehavior):

    def __init__(self, name, **kwargs):

        super().__init__(**kwargs)
        self.name = name
        self.add_widget(Label(text = str(name)))
        print(self.name)

    def on_enter(self):

        for i in self.children:

            i.color = (1, 0, 0, 1)
    
    def on_leave(self):

        for i in self.children:

            i.color = (0, 1, 0, 1)

    def on_release(self):

        content = Label(text = self.name)
        self.popup = Popup(content = content, size_hint = (.6, .8), title = '')
        self.popup.open()
        print(self.name)
        
class B(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        for i in range(10):

            self.add_widget(A(name = str(i), size_hint_y = .1))

class myApp(App):

    def build(self):

        return B()

if __name__ == '__main__':

    myApp().run()