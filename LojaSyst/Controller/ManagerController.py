import os
from os.path import dirname

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.config import Config
from Controller.ClienteController import TelaCadastroCliente
from Controller.ClienteController import TelaListaCliente
from Controller.EquipamentoController import TelaCadastroEquipamento
from Controller.MarcaController import TelaCadastroMarca
from Controller.ResponsavelController import TelaCadastroResponsavel
from Controller.ServiceController import TelaCadastroService

Config.set('graphics', 'resizable', False)
Window.size = (1000, 800)

'''
CARREGANDO ARQUIVOS KV
'''

Builder.load_file(os.path.join(dirname(__file__), '../KViews/manager.kv'))

Builder.load_file(os.path.join(dirname(__file__), '../KViews/Cliente/cadastro.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/Cliente/lista.kv'))

Builder.load_file(os.path.join(dirname(__file__), '../KViews/Equipamento/cadastro.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/Equipamento/lista.kv'))

Builder.load_file(os.path.join(dirname(__file__), '../KViews/Service/cadastro.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/Service/lista.kv'))

Builder.load_file(os.path.join(dirname(__file__), '../KViews/Responsavel/cadastro.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/Responsavel/lista.kv'))

Builder.load_file(os.path.join(dirname(__file__), '../KViews/Marca/cadastro.kv'))
Builder.load_file(os.path.join(dirname(__file__), '../KViews/Marca/lista.kv'))




class GerenciarTelas(ScreenManager):
    pass

class TelaMenu(Screen):
    def __init__(self, **kwargs):
        super(TelaMenu, self).__init__(**kwargs)

    #CLientes
    def changetoCad_Cliente(self):
        self.manager.current = 'telacad_cliente'
    def changetoList_Cliente(self):
        self.manager.current = 'telalist_cliente'

    #Equipamento
    def changetoCad_Equipamento(self):
        self.manager.current = 'telacad_Equip'
    def changetoList_Equipamento(self):
        self.manager.current = 'telalist_equip'

    #Serivços
    def changetoCad_Service(self):
        self.manager.current = 'telacad_service'
    def changetoList_Service(self):
        self.manager.current = 'telalist_service'


    #Marca
    def changetoCad_Marca(self):
        self.manager.current = 'telacad_marca'
    def changetoList_Marca(self):
        self.manager.current = 'telalist_marca'


    #Responsaveis
    def changetoCad_Tecnico(self):
        self.manager.current = 'telacad_respons'
    def changetoList_Tecnico(self):
        self.manager.current = 'telalist_respons'




class AppExec(App):
    def build(self):
        return GerenciarTelas()

