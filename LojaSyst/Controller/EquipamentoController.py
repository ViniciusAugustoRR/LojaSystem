import os
from os.path import dirname
from random import sample

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
#from kivy.lang import Builder
from Models.Equipamento import EquipamentoMD
from BD.BD import DBfac
from kivy.clock import Clock


'''
TELA DE CADASTRO DE EQUIPAMENTO
'''

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




'''
TELA DE LISTAGEM EQUIPAMENTOS
'''

class TelaListaEquipamento(Screen):
    def __init__(self, **kwargs):
        super(TelaListaEquipamento, self).__init__(**kwargs)


    def changetoMenu(self):
        self.manager.current = 'telamenu'



class Rowp_equip(BoxLayout):
    linha_cont_equip = ObjectProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.concluirInit, 0)

    def concluirInit(self, dt):
        for equip in self.linha_cont_equip:

            self.add_widget(Button(text=equip.Nome))
            self.add_widget(Button(text="Edit", size_hint_x=0.3))
            self.add_widget(Button(text='Delete', size_hint_x=0.3))


class Lista_Equip(RecycleView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        db = DBfac()
        equips = db.ConsultarEquipamentos()
        for c in equips:
            print(c.Nome)

        self.data = [{'linha_cont_equip': [equip]} for equip in equips]


        print(self.data)


