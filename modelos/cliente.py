from modelos.entidad import Entidad

class Cliente(Entidad):

    def __init__(self, codigo, nombre, documento, telefono, correo):
        super().__init__(codigo)

        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono
        self.correo = correo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if len(valor.strip()) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres.")
        self.__nombre = valor

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):
        if not str(valor).isdigit():
            raise ValueError("Documento inválido.")
        self.__documento = valor

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        if not str(valor).isdigit():
            raise ValueError("Teléfono inválido.")
        self.__telefono = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if "@" not in valor:
            raise ValueError("Correo electrónico inválido.")
        self.__correo = valor

    def mostrar_informacion(self):
        return (
            f"""
Código: {self.codigo}
Nombre: {self.nombre}
Documento: {self.documento}
Teléfono: {self.telefono}
Correo: {self.correo}
"""
        )