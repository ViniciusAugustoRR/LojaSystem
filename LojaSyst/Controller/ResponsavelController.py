from kivy.graphics.context import Clock
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
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


'''
    TELA DE LISTA DE RESPONSAVEIS
'''

class TelaListaResponsavel(Screen):
    def __init__(self, **kwargs):
        super(TelaListaResponsavel, self).__init__(**kwargs)

    def changetoMenu(self):
        self.manager.current = 'telamenu'



class Rowp_Respons(BoxLayout):
    linha_cont_respons = ObjectProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.concluirInit, 0)

    def concluirInit(self, dt):
        for respons in self.linha_cont_marca:

            self.add_widget(Button(text=respons.Nome))
            self.add_widget(Button(text="Edit", size_hint_x=0.3))
            self.add_widget(Button(text='Delete', size_hint_x=0.3))



class ListaResponsavel(RecycleView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        db = DBfac()
        reponsaveis = db.ConsultarTecnicos()
        for repsons in reponsaveis:
            print(repsons.Nome)

        self.data = [{'linha_cont_marca': [respons]} for respons in reponsaveis]
        print(self.data)


