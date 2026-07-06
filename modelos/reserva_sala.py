# Importa la clase Servicio
from modelos.servicio import Servicio

# Clase que representa el servicio de reserva de salas
class ReservaSala(Servicio):

    # Constructor
    def __init__(self, codigo, nombre, costo_base, capacidad):

        super().__init__(codigo, nombre, costo_base)
        self.capacidad = capacidad

    # Calcula el costo de la reserva
    def calcular_costo(self):

        return self.costo_base + (self.capacidad * 5)

    # Devuelve la descripcion del servicio
    def descripcion(self):

        return f"Reserva de sala para {self.capacidad} personas"