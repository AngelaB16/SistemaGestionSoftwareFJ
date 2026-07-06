# Importa la clase Servicio
from modelos.servicio import Servicio

# Clase para asesorias especializadas
class Asesoria(Servicio):

    # Constructor
    def __init__(self, codigo, nombre, costo_base, horas):

        super().__init__(codigo, nombre, costo_base)
        self.horas = horas

    # Calcula el costo de la asesoría
    def calcular_costo(self):

        return self.costo_base * self.horas

    # Devuelve la descripción
    def descripcion(self):

        return f"Asesoría especializada de {self.horas} hora(s)."