import os
from os.path import dirname

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.config import Config
from Controller.CadastroController import TelaCadastro

Config.set('graphics', 'resizable', False)
Window.size = (1000, 800)

Builder.load_file(os.path.join(dirname(__file__), '../KViews/manager.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/cadastro.kv'))

class GerenciarTelas(ScreenManager):
    pass

class TelaMenu(Screen):
    def __init__(self, **kwargs):
        super(TelaMenu, self).__init__(**kwargs)

    def changetoCad(self):
        self.manager.current = 'telacad'



class AppExec(App):
    def build(self):
        return GerenciarTelas()

