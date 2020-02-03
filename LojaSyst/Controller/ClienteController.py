from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, BooleanProperty
from Models.Cliente import ClienteMD
from BD.BD import DBfac
from kivy.clock import Clock



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


class AnchorCliente(BoxLayout):
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
    def __init__(self, **kwargs):
        super(TelaListaCliente, self).__init__(**kwargs)


    def changetoMenu(self):
        self.manager.current = 'telamenu'



class Rowp(BoxLayout):
    linha_cont = ObjectProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.concluirInit, 0)

    def concluirInit(self, dt):
        for cliente in self.linha_cont:

            self.add_widget(Button(text=cliente.Nome_c))
            self.add_widget(Button(text="Edit", size_hint_x=0.3))
            self.add_widget(Button(text='Delete', size_hint_x=0.3))





class Lista(RecycleView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        db = DBfac()
        clientes = db.ConsultarClientes()
        for c in clientes:
            print(c.Nome_c)

        self.data = [{'linha_cont': [cliente]} for cliente in clientes]


        print(self.data)












