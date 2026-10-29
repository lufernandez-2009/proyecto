import os

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from clases.usuario import Usuario

# Carga el archivo registro.kv, que está en esta misma carpeta
Builder.load_file(os.path.join(os.path.dirname(__file__), "registro.kv"))


# El nombre de esta clase (RegistroScreen) es el mismo que aparece entre < > en registro.kv.
# MDScreen es la clase de KivyMD que representa una pantalla completa.
class RegistroScreen(MDScreen):
    # Se ejecuta cuando en el .kv se escribe root.volver()
    # "inicio" es el nombre con el que se agregó InicioScreen en app.py.
    def volver(self):
        self.manager.current = "inicio"

    # Se ejecuta cuando en el .kv se escribe root.registrar()
    def registrar(self):
        # Obtenemos la aplicación y los datos escritos en los campos
        app = MDApp.get_running_app()

        nombre = self.ids.nombre.text.strip()
        edad = self.ids.edad.text.strip()
        correo = self.ids.correo.text.strip()
        contrasena = self.ids.contrasena.text

        # Creamos un objeto Usuario con los datos del formulario
        usuario = Usuario(nombre, edad, correo, contrasena)

        # 1. Validar que los datos estén completos
        if not usuario.datos_completos():
            print("Registro inválido: completá todos los campos.")
            return

        # 2. Validar que el correo sea válido
        if not usuario.correo_valido():
            print("Registro inválido: el correo debe terminar en @pioix.edu.ar.")
            return

        # 3. Validar que el nombre sea válido
        if not usuario.nombre_valido():
            print("Registro inválido: el nombre solo puede contener letras y espacios.")
            return

        # 4. Comprobar que no exista otro usuario con el mismo correo
        for registrado in app.usuarios:
            if registrado.correo.lower() == usuario.correo.lower():
                print("Registro inválido: ya existe un usuario con ese correo.")
                return

        # 5. Si todas las validaciones son correctas, guardamos el usuario
        app.usuarios.append(usuario)
        print("Registro válido: usuario registrado correctamente.")

        # Pasamos a la pantalla Login
        self.manager.current = "login"
