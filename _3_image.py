from kivy.app import App
from kivy.uix.image import Image,AsyncImage

class myApp(App):
    def build(self):
        img_1 = Image(source="./1.png")
        img_2 = AsyncImage(
            source="https://www.adobe.com/content/dam/cc/us/en/creativecloud/illustration-adobe-illustration/how-to-draw-trees/draw-trees_fb-img_1200x800.jpg"
            ,size_hint=(None,None),width=100,height=50
            )
        return img_2

myApp().run()