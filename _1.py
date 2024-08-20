from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

#background color
Window.clearcolor = (1,1,1,1)

# title of app = what is written before App in class name

class myApp(App):
    def build(self):
        label = Label(text="Hello kivy",font_size='120sp',bold=True,color=(1,0,0,1))   #color(r,g,b,opacity)
        return label

myApp().run()

