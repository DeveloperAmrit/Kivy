from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

class myApp(App):
    def build(self):
        
        page_layout_1 = PageLayout()

        btn_1 = Button(text='Button 1')
        btn_2 = Button(text='Button 2')

        page_layout_1.add_widget(btn_1)
        page_layout_1.add_widget(btn_2)

        return page_layout_1

myApp().run()