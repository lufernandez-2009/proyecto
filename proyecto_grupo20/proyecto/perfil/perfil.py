import os

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

# Carga el archivo perfil.kv, que está en esta misma carpeta
Builder.load_file(os.path.join(os.path.dirname(__file__), "perfil.kv"))


# El nombre de esta clase (PerfilScreen) es el mismo que aparece entre < > en perfil.kv.
class PerfilScreen(MDScreen):
    # Se ejecuta cuando en el .kv se escribe root.volver()
    # "home" es el nombre con el que se agregó HomeScreen en app.py.
    def volver(self):
        self.manager.current = "home"

    # Cerrar sesión y volver a la pantalla de Inicio
    def cerrar_sesion(self):
        self.manager.current = "inicio"