from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.clock import Clock
from BD.BD import DBfac
from Models.Cliente import ClienteMD

kv = """
<Row>:
    id: row
    canvas.before:
        Color:
            rgba: 0.5, 0.5, 0.5, 1
        Rectangle:
            size: self.size
            pos: self.pos


<Test>:
    canvas:
        Color:
            rgba: 0.3, 0.3, 0.3, 1
        Rectangle:
            size: self.size
            pos: self.pos
    orientation: 'vertical'
    
    RecycleView:
        id: rvlist
        scroll_type: ['bars', 'content']
        scroll_wheel_distance: dp(114)
        bar_width: dp(10)
        viewclass: 'Row'
        RecycleBoxLayout:
            default_size: None, dp(40)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            spacing: dp(2)
"""



Builder.load_string(kv)


class Row(BoxLayout):
    row_content = ObjectProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.concluir_init, 0)

    def concluir_init(self, dt):
        for cliente in self.row_content:
            self.orientation = 'horizontal'
            print()
            self.add_widget(Label(text=cliente.Nome_c))
            self.add_widget(Button(text="Edit"))
            self.add_widget(Button(text='Delete'))




class Test(BoxLayout):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        db = DBfac()
        Clientes = db.ConsultarClientes()
        for c in Clientes:
            print(c.Nome_c)

        self.ids.rvlist.data = [{'row_content': [cliente]} for cliente in Clientes]



class princ(App):
    def build(self):
        return Test()


if __name__ == '__main__':
    princ().run()




