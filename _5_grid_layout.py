from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class myApp(App):
    def build(self):
                                       # to enable customization  # height
        grid_1 = GridLayout(cols=2, row_force_default=True,row_default_height=40)
        btn_1 = Button(text="Button 1")
        btn_2 = Button(text="Button 2")
        btn_3 = Button(text="Button 3")
        btn_4 = Button(text="Button 4")
        btn_5 = Button(text="Button 5")

        grid_1.add_widget(btn_1)
        grid_1.add_widget(btn_2)
        grid_1.add_widget(btn_3)
        grid_1.add_widget(btn_4)
        grid_1.add_widget(btn_5)

        return grid_1

myApp().run()
