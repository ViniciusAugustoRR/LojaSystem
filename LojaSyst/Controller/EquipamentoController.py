import os
from os.path import dirname
from random import sample


from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from Models.Equipamento import EquipamentoMD
from BD.BD import DBfac
from string import ascii_lowercase



class TelaCadastroEquipamento(Screen):
    def __init__(self, **kwargs):
        super(TelaCadastroEquipamento, self).__init__(**kwargs)


    def changetoMenu(self):
        self.manager.current = 'telamenu'


class AnchorB(BoxLayout):
    def cadastrar(self):

        ClienteEx = EquipamentoMD()


        DB1 = DBfac()

        DB1.CadastrarCliente(ClienteEx)