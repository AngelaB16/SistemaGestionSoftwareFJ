# Importa las clases necesarias para crear clases abstractas
from abc import ABC, abstractmethod

# Clase abstracta que representa un servicio del sistema
class Servicio(ABC):

    # Constructor
    def __init__(self, codigo, nombre, costo_base):

        self.codigo = codigo
        self.nombre = nombre
        self.costo_base = costo_base

    # Propiedad codigo
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):

        if not valor:
            raise ValueError("El código es obligatorio.")

        self.__codigo = valor

    # Propiedad nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        if len(valor.strip()) < 3:
            raise ValueError("Nombre del servicio inválido.")

        self.__nombre = valor

    # Propiedad costo
    @property
    def costo_base(self):
        return self.__costo_base

    @costo_base.setter
    def costo_base(self, valor):

        if valor <= 0:
            raise ValueError("El costo debe ser mayor que cero.")

        self.__costo_base = valor

    # Metodo abstracto que calculara el costo
    @abstractmethod
    def calcular_costo(self):
        pass

    # Metodo abstracto para describir el servicio
    @abstractmethod
    def descripcion(self):
        pass