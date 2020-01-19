import os
from os.path import dirname

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from Models.Cliente import ClienteMD


#Builder.load_file(os.path.join(dirname(__file__), '../KViews/cadastro.kv'))
#Builder.load_file(os.path.join(dirname(__file__), '../KViews/manager.kv'))


class TelaCadastro(Screen):
    def __init__(self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)

    def changetoTest(self):
        self.manager.current = 'telamenu'


class AnchorB(BoxLayout):
    def cadastrar(self):
        ClienteEx = ClienteMD()
        ClienteEx.Nome_c = self.ids.camponome.text
        ClienteEx.Email = self.ids.campoemail.text
        ClienteEx.Telefone = self.ids.campotelef.text
        ClienteEx.Enderec = self.ids.campoender.text

