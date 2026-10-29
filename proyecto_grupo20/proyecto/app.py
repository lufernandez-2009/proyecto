#Importaciones necesarias para la aplicación: Window, MDApp, MDScreenManager
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

#Importamos las pantallas que vamos a usar en la aplicación.
# Cada pantalla está en su propia carpeta
# from carpeta.archivo import Clase
from inicio.inicio import InicioScreen
from registro.registro import RegistroScreen
from home.home import HomeScreen
from login.login import LoginScreen
from perfil.perfil import PerfilScreen
from programadores.programadores import ProgramadoresScreen
from clases.usuario import Usuario

# Tamaño de la ventana (ancho, alto)
Window.size = (1000, 600)

# Clase principal de la aplicación. Hereda de MDApp, que es la clase base para aplicaciones KivyMD.
class App(MDApp):
    def build(self):
        self.title = "Proyecto Integrador" #Titulo de la ventana
        self.theme_cls.primary_palette = "Pink" #Paleta de colores principal (Teal es verde azulado)
        self.theme_cls.theme_style = "Light" #Estilo del tema (Light es claro, Dark es oscuro)

        # Lista donde se guardan los usuarios registrados
        self.usuarios = []

        # Usuario de prueba para comprobar el inicio de sesión
        usuario_prueba = Usuario(
            "Nombre Apellido",
            "18",
            "napellidoa@pioix.edu.ar",
            "1234"
        )
        self.usuarios.append(usuario_prueba)

        # Usuario que inició sesión
        self.usuario_actual = None

        # El administrador de pantallas guarda todas las pantallas y muestra una a la vez. 
        administrador = MDScreenManager() #MDScreenManager() es una clase que permite manejar varias pantallas en la aplicación.

        #add_widget() agrega una pantalla al administrador de pantallas.
        # El nombre de la pantalla (name="...") es el que se usa para navegar entre pantallas:
        # cuando en el código aparece manager.current = "home", se muestra la pantalla que se agregó con name="home".
        administrador.add_widget(InicioScreen(name="inicio"))
        administrador.add_widget(RegistroScreen(name="registro"))
        administrador.add_widget(HomeScreen(name="home"))
        administrador.add_widget(LoginScreen(name="login"))
        administrador.add_widget(PerfilScreen(name="perfil"))
        administrador.add_widget(ProgramadoresScreen(name="programadores"))

        # Retorna el administrador de pantallas para que la aplicación lo use como pantalla principal.
        return administrador


if __name__ == "__main__":
    # Ejecuta/corre la aplicación
    App().run()