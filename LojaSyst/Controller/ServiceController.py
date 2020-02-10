from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from Models.Service import ServiceMD
from BD.BD import DBfac
import re
from datetime import datetime
from datetime import date


class TelaCadastroService(Screen):
    def __init__(self, **kwargs):
        super(TelaCadastroService, self).__init__(**kwargs)


    def changetoMenu(self):
        self.manager.current = 'telamenu'


class AnchorService(BoxLayout):

    def cadastrar(self):

        service = ServiceMD()

        service.Data_i = self.convertDateTime(self.ids.campodatai.text, self.ids.campohorai.text)
        service.Data_i = self.convertDateTime(self.ids.campodataf.text, self.ids.campohoraf.text)
        print(service.Data_i)
        print(service.Data_f)

        service.Cliente_Id = int(self.ids.campocliente.text)
        service.Responsavel_Id = int(self.ids.camporespons.text)
        service.Equipamento_Id = int(self.ids.campoequip.text)

        DB1 = DBfac()

        DB1.CadastrarService(service)

    def convertDateTime(self, data: str, hora: str):

        datastr = list(re.split("/|:| ", data + " " + hora))
        dataint = []

        for item in datastr:
            dataint.append(int(item))

        datatuple = tuple(dataint)

        return datetime(datatuple).strftime("%d/%m/%Y %H:%M:%S")


'''
TELA DE LISTA DE CLIENTES
'''

class TelaListaService(Screen):
    def __init__(self, **kwargs):
        super(TelaListaService, self).__init__(**kwargs)


    def changetoMenu(self):
        self.manager.current = 'telamenu'



class RowServs(BoxLayout):
    linha_cont_service = ObjectProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.concluirInit, 0)

    def concluirInit(self, instance):
        for service in self.linha_cont_service:

            self.add_widget(Button(text=str(service.Id)))
            self.add_widget(Button(text="Edit", size_hint_x=0.3, on_release=self.edit))
            self.add_widget(Button(text='Delete', size_hint_x=0.3, on_release=self.delet))

    def edit(self, instance):
        print('edit')

    def delet(self, instance):
        print('delete')


class ListaServs(RecycleView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        db = DBfac()
        services = db.ConsultarServices()
        print(services)

        self.data = [{'linha_cont_service': [service]} for service in services]

