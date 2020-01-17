import os
from os.path import dirname

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Window.size = (1240, 860)


#Builder.load_file('cadastro.kv')


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)


class Cad(App):
    def build(self):
        return Builder.load_file(
            os.path.join(dirname(__file__), 'cadastro.kv')
        )





