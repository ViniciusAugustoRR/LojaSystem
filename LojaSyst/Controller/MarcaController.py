
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from Models.Marca import MarcaMd
from BD.BD import DBfac


class TelaCadastroMarca(Screen):
    def __init__(self, **kwargs):
        super(TelaCadastroMarca, self).__init__(**kwargs)


    def changetoMenu(self):
        self.manager.current = 'telamenu'


class AnchorMarca(BoxLayout):
    def cadastrar(self):

        marca = MarcaMd()

        marca.Nome_Marca = self.ids.camponome.text

        DB1 = DBfac()

        DB1.CadastrarMarca(marca)