import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen

Window.clearcolor = (1,1,1, 1)
Window.size=(300,600)
class MW(ScreenManager):
    pass
class Intm(Screen):
    pass
class Lm(Screen):
    pass
class La(Screen):
    pass
class QA(Screen):
    pass
class Intf(Screen):
    pass
class Ints(Screen):
    pass
class Intt(Screen):
    pass
class Siu(Screen):
    pass
class Fw(Screen):
    pass
class Ero(Screen):
    pass
class Sw(Screen):
    pass
class Tw(Screen):
    pass
class MApp(Screen):
    pass


class Myapp(App):
    def build(self):
        self.arr=['','','','','','','','','','','']
        kv= Builder.load_file("main.kv")
        return kv
if __name__=="__main__":
    Myapp().run()
