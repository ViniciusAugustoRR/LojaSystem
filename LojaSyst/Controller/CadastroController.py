import os
from os.path import dirname

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.config import Config
from kivy.resources import resource_add_path


Config.set('graphics', 'resizable', False)
Window.size = (800, 600)

#Builder.load_file('manager.kv')

Builder.load_file(os.path.join(dirname(__file__), '../KViews/cadastro.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/manager.kv'))


class GerenciarTelas(ScreenManager):
    pass

class TelaCadastro(Screen):
    def __init__(self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)

    def changetoTest(self):
        self.manager.current = 'telatest'


class TelaTest(Screen):
    def __init__(self, **kwargs):
        super(TelaTest, self).__init__(**kwargs)

    def changetoCad(self):
        self.manager.current = 'telacad'


class Cad(App):
    def build(self):

        return GerenciarTelas() #Builder.load_file())

Cad().run()
