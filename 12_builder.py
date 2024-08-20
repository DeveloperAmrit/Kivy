from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

mydoc = '''
Label:
    text:"What is written in .kv can be written here"
'''

class _12App(App):
    def build(self):
        # for writing .kv here
        builder_1 = Builder.load_string(mydoc)

        # for linking any .kv file
        builder_2 = Builder.load_file('./12.kv')

        # trying to merge
        l1 = BoxLayout(orientation='vertical')
        l1.add_widget(builder_1)
        l1.add_widget(builder_2)

        #* Ya both can be merged , before is which is before added to layout
        
        return l1
    
_12App().run()