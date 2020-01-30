import os
from os.path import dirname

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.config import Config
from Controller.ClienteController import TelaCadastroCliente
from Controller.ClienteController import TelaListaCliente

Config.set('graphics', 'resizable', False)
Window.size = (1000, 800)

Builder.load_file(os.path.join(dirname(__file__), '../KViews/manager.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/Cliente/cadastro.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/Cliente/lista.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/Equipamento/cadastro.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/Equipamento/lista.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/Service/cadastro.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/Service/lista.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/Tecnico/cadastro.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/Tecnico/lista.kv'))




class GerenciarTelas(ScreenManager):
    pass

class TelaMenu(Screen):
    def __init__(self, **kwargs):
        super(TelaMenu, self).__init__(**kwargs)

    def changetoCad_Cliente(self):
        self.manager.current = 'telacad_cliente'

    def changetoList_Cliente(self):
        self.manager.current = 'telalist_cliente'





class AppExec(App):
    def build(self):
        return GerenciarTelas()

