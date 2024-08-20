from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class myApp(App):
    def build(self):
        """
        Cannot do 
        return b1,b2 
        so rap in a layout and return it.
        """        
        layout_1 = BoxLayout(orientation='vertical',padding=10)

        b1 = Button(text="Button 1")
        b2 = Button(text="Button 2")

        layout_1.add_widget(b1)
        layout_1.add_widget(b2)
        return layout_1

myApp().run()