class Usuario:
    def __init__(self, nombre, edad, correo, contrasena):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.contrasena = contrasena

    def datos_completos(self):
        atributos = [self.nombre, self.edad, self.correo, self.contrasena]
        for dato in atributos:
            if str(dato).strip() == "":
                return False
        return True

    def correo_valido(self):
        if not self.correo:
            return False
        return self.correo.endswith("@pioix.edu.ar")

    def nombre_valido(self):
        if not self.nombre or not isinstance(self.nombre, str):
            return False
        nombre_sin_espacios = self.nombre.replace(" ", "")
        return nombre_sin_espacios.isalpha()

    def contrasena_correcta(self, contrasena):
        return self.contrasena == contrasena