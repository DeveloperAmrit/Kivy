from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class myApp(App):
    def build(self):
        b1 = Button(text="Click me",size_hint=(0.2,0.1),pos_hint={"center_x":0.5,"center_y":0.5}
                    ,on_press = self.b1_click,on_release = self.b1_released)
        return b1
    
    def b1_click(self,b1):
        print('b1 clicked')
    def b1_released(self,b1):
        print('b1 released')
    
myApp().run()