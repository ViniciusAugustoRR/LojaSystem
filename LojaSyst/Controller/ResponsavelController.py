
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from Models.Responsavel import ResponsavelMD
from BD.BD import DBfac



class TelaCadastroResponsavel(Screen):
    def __init__(self, **kwargs):
        super(TelaCadastroResponsavel, self).__init__(**kwargs)


    def changetoMenu(self):
        self.manager.current = 'telamenu'


class AnchorResponsavel(BoxLayout):
    def cadastrar(self):

        respons = ResponsavelMD()

        respons.Nome = self.ids.camponome.text
        respons.Categoria = self.ids.campocateg.text

        DB1 = DBfac()

        DB1.CadastrarTecnico(respons)
