from abc import ABC, abstractmethod


class Entidad(ABC):

    #Clase abstracta base para las entidades del sistema.
    
    def __init__(self, codigo):
        self._codigo = codigo

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
        
        #Método que debe implementar cada clase hija.
        
        pass