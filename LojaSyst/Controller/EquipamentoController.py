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


class AnchorEquip(BoxLayout):
    def cadastrar(self):

        Equipamento = EquipamentoMD()

        Equipamento.Serie_N = self.ids.camponserie.text
        Equipamento.Nome = self.ids.equipcamponome.text
        Equipamento.Acessorios = self.ids.campoacessorios.text
        Equipamento.Modelo = self.ids.campomodelo.text
        Equipamento.Marca_id = int(self.ids.campomarca.text)

        DB1 = DBfac()

        DB1.CadastrarEquipamento(Equipamento)