from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class myApp(App):
    def build(self):
        float_layout_1 = FloatLayout()

        btn_1 = Button(text='Button 1',pos_hint={"center_x":0.5,"center_y":0.1},size_hint=(0.5,0.5))

        float_layout_1.add_widget(btn_1)
        return float_layout_1
    

myApp().run()
"""
box_layout = flex
grid_layout = grid
float_layout = absolute
"""