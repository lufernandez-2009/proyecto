import os

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

# Carga el archivo home.kv, que está en esta misma carpeta
Builder.load_file(os.path.join(os.path.dirname(__file__), "home.kv"))


# El nombre de esta clase (HomeScreen) es el mismo que aparece entre < > en home.kv.
class HomeScreen(MDScreen):
    # Se ejecuta cuando en el .kv se escribe root.ir_a_perfil()
    # self.manager.current cambia la pantalla que se muestra por la que tiene ese nombre.
    def ir_a_perfil(self):
        self.manager.current = "perfil"

    # Se ejecuta cuando en el .kv se escribe root.opcion_1()
    def opcion_1(self):
        # Texto de relleno. Cuando se elija el dataset, esta opción
        # va a llevar a una pantalla real del sistema.
        self.manager.current = "perfil"

    # Se ejecuta cuando en el .kv se escribe root.opcion_2()
    def opcion_2(self):
        self.manager.current = "perfil"