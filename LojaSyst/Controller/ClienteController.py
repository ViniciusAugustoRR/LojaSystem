import os
from os.path import dirname
from random import sample


from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from Models.Cliente import ClienteMD
from BD.BD import DBfac
from string import ascii_lowercase


#Builder.load_file(os.path.join(dirname(__file__), '../KViews/Cliente/lista.kv'))
#Builder.load_file(os.path.join(dirname(__file__), '../KViews/manager.kv'))

'''
TELA DE CADASTRO DE CLIENTES
'''

class TelaCadastroCliente(Screen):
    def __init__(self, **kwargs):
        super(TelaCadastroCliente, self).__init__(**kwargs)


    def changetoMenu(self):
        self.manager.current = 'telamenu'


class AnchorB(BoxLayout):
    def cadastrar(self):

        ClienteEx = ClienteMD()
        ClienteEx.Nome_c = self.ids.camponome.text
        ClienteEx.Email = self.ids.campoemail.text
        ClienteEx.Telefone = self.ids.campotelef.text
        ClienteEx.Enderec = self.ids.campoender.text

        DB1 = DBfac()

        DB1.CadastrarCliente(ClienteEx)




'''
TELA DE LISTA DE CLIENTES
'''

class TelaListaCliente(Screen):
    list_tela = ObjectProperty()

    def __init__(self, **kwargs):
        super(TelaListaCliente, self).__init__(**kwargs)


    def popular(self):
        print(self.ids)

class Lista(BoxLayout):
    list_box = ObjectProperty()
        #self.ids.rv.data = [{'value': ''.join(sample(ascii_lowercase, 6))} for x in range(50)]