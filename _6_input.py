from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class myApp(App):
    def build(self):
        box_layout_1 = BoxLayout(orientation="vertical",padding=200,spacing=50)

        self.user_name = TextInput(text="Enter your user name")         # To use globally in class use self.
        self.password = TextInput(text="Enter password")
        self.btn_1_submit = Button(text="Log in",on_press=self.submit_btn_1)

        box_layout_1.add_widget(self.user_name)
        box_layout_1.add_widget(self.password)
        box_layout_1.add_widget(self.btn_1_submit)

        return box_layout_1

    def submit_btn_1(self,obj):
        print(f'Your user name is {self.user_name.text}')
        print(f'Your password is {self.password.text}')

myApp().run()