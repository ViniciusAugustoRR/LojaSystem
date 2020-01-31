
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from Models.Service import ServiceMD
from BD.BD import DBfac



class TelaCadastroService(Screen):
    def __init__(self, **kwargs):
        super(TelaCadastroService, self).__init__(**kwargs)


    def changetoMenu(self):
        self.manager.current = 'telamenu'


class AnchorService(BoxLayout):
    def cadastrar(self):

        service = ServiceMD()


        DB1 = DBfac()

        DB1.CadastrarCliente(service)

