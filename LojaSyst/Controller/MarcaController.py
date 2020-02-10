from kivy.graphics.context import Clock
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
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



'''
TELA DE LISTA DE MARCAS
'''

class TelaListaMarcas(Screen):
    def __init__(self, **kwargs):
        super(TelaListaMarcas, self).__init__(**kwargs)


    def changetoMenu(self):
        self.manager.current = 'telamenu'



class Rowp_Marca(BoxLayout):
    linha_cont_marca = ObjectProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.concluirInit, 0)


    def concluirInit(self, dt):

        for marca in self.linha_cont_marca:
            self.add_widget(Button(text=marca.Nome_Marca))
            self.add_widget(Button(text="Edit", size_hint_x=0.3))
            self.add_widget(Button(text='Delete', size_hint_x=0.3))



class ListaMarcas(RecycleView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        db = DBfac()
        marcas = db.ConsultarMarcas()


        self.data = [{'linha_cont_marca': [marca]} for marca in marcas]

