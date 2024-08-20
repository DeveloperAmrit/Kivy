from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class myApp(App):
    def build(self):
        
        anchor_layout_1 = AnchorLayout(anchor_x='right',anchor_y='bottom')

        btn_1 = Button(text='Button 1',size_hint=(None,None),width=100,height=50)

        anchor_layout_1.add_widget(btn_1)
        
        return anchor_layout_1

myApp().run()