import os

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

# Carga el archivo inicio.kv, que está en esta misma carpeta
Builder.load_file(os.path.join(os.path.dirname(__file__), "inicio.kv"))


# El nombre de esta clase (InicioScreen) es el mismo que aparece entre < > en inicio.kv.
# Así Kivy sabe que el diseño de ese archivo pertenece a esta pantalla.
class InicioScreen(MDScreen):
    # Cada método se puede llamar desde el .kv escribiendo root.nombre_del_metodo()
    # (por ejemplo, root.ir_a_login() dentro de un on_release).

    # self.manager es el administrador de pantallas creado en app.py.
    # Su propiedad "current" guarda el nombre de la pantalla que se está mostrando.
    # Al cambiarla, la aplicación pasa a mostrar la pantalla con ese nombre.
    def ir_a_login(self):
        self.manager.current = "login"

    def ir_a_registro(self):
        self.manager.current = "registro"

    def ir_a_programadores(self):
        self.manager.current = "programadores"
