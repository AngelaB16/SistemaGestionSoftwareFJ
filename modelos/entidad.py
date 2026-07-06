from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, codigo):
        self.codigo = codigo

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not valor:
            raise ValueError("El código no puede estar vacío.")

        self._codigo = valor

    @abstractmethod
    def mostrar_informacion(self):
        pass