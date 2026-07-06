# Importa datetime para registrar la fecha de la reserva
from datetime import datetime

# Clase que representa una reserva
class Reserva:

    # Constructor
    def __init__(self, codigo, cliente, servicio, duracion):

        self.codigo = codigo
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.fecha = datetime.now()

    # Confirma la reserva
    def confirmar(self):

        self.estado = "Confirmada"

    # Cancela la reserva
    def cancelar(self):

        self.estado = "Cancelada"

    # Procesa la reserva
    def procesar(self):

        if self.estado == "Cancelada":
            raise Exception("No es posible procesar una reserva cancelada.")

        self.confirmar()

    # Calcula el costo total
    def costo_total(self):

        return self.servicio.calcular_costo() * self.duracion

    # Devuelve la información de la reserva
    def mostrar_informacion(self):

        return (
            f"\nReserva: {self.codigo}"
            f"\nCliente: {self.cliente.nombre}"
            f"\nServicio: {self.servicio.nombre}"
            f"\nDuración: {self.duracion}"
            f"\nEstado: {self.estado}"
            f"\nCosto Total: ${self.costo_total():,.2f}"
        )