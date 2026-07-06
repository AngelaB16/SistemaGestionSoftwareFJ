# Importa la clase Servicio
from modelos.servicio import Servicio

# Clase para alquiler de equipos
class AlquilerEquipo(Servicio):

    # Constructor
    def __init__(self, codigo, nombre, costo_base, dias):

        super().__init__(codigo, nombre, costo_base)
        self.dias = dias

    # Calcula el costo total
    def calcular_costo(self):

        return self.costo_base * self.dias

    # Devuelve la descripcion
    def descripcion(self):

        return f"Alquiler por {self.dias} día(s)."