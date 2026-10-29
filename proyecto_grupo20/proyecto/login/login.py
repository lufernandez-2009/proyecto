import os

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

# Carga el diseño de la pantalla Login
Builder.load_file(
    os.path.join(os.path.dirname(__file__), "login.kv")
)


class LoginScreen(MDScreen):

    # Volver a la pantalla de Inicio
    def volver(self):
        self.manager.current = "inicio"

    # Iniciar sesión y entrar a Home
    def login(self):
        app = MDApp.get_running_app()

        # Leer los datos escritos en los campos
        correo = self.ids.correo.text.strip()
        contrasena = self.ids.contrasena.text

        # 1. Validar que los campos no estén vacíos
        if correo == "" or contrasena.strip() == "":
            print("Inicio de sesión inválido: completá todos los campos.")
            return

        # 2. Buscar un usuario con ese correo
        usuario_encontrado = None

        for usuario in app.usuarios:
            if usuario.correo.lower() == correo.lower():
                usuario_encontrado = usuario
                break

        if usuario_encontrado is None:
            print("Inicio de sesión inválido: no existe un usuario con ese correo.")
            return

        # 3. Validar que la contraseña sea correcta
        if not usuario_encontrado.contrasena_correcta(contrasena):
            print("Inicio de sesión inválido: contraseña incorrecta.")
            return

        # 4. Guardar el usuario actual
        app.usuario_actual = usuario_encontrado

        print("Inicio de sesión válido: ¡bienvenido!")

        # Pasar a Home
        self.manager.current = "home"