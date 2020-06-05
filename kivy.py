from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview import RecycleView
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (
    BooleanProperty, StringProperty,
     NumericProperty, ObjectProperty
    )

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



class A(BoxLayout, HoverBehavior, ButtonBehavior):

    def __init__(self, name, **kwargs):

        super().__init__(**kwargs)
        self.name = name

    def on_enter(self):

        for i in self.children:

            i.color = (1, 1, 1, 1)
    
    def on_leave(self):

        for i in self.children:

            i.color = (.06, .45, .45, 1)

    def on_release(self):
        print(self.name)
        
class myApp(App):

    def build(self):

        return A('salam')

if __name__ == '__main__':

    myApp().run()