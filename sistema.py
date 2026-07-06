# Clase encargada de administrar toda la logica

from logger_config import registrar_evento, registrar_error
from excepciones import ClienteError, ServicioError, ReservaError


class Sistema:

    # Constructor
    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

    # CLIENTES

    def agregar_cliente(self, cliente):

        try:

            for c in self.clientes:

                if c.documento == cliente.documento:
                    raise ClienteError("El cliente ya se encuentra registrado.")

            self.clientes.append(cliente)

            registrar_evento(f"Cliente registrado: {cliente.nombre}")

        except Exception as error:

            registrar_error(str(error))
            raise

    def obtener_clientes(self):

        return self.clientes

    # SERVICIOS

    def agregar_servicio(self, servicio):

        try:

            self.servicios.append(servicio)

            registrar_evento(f"Servicio agregado: {servicio.nombre}")

        except Exception as error:

            registrar_error(str(error))
            raise

    def obtener_servicios(self):

        return self.servicios

    # RESERVAS

    def agregar_reserva(self, reserva):

        try:

            self.reservas.append(reserva)

            registrar_evento(f"Reserva creada: {reserva.codigo}")

        except Exception as error:

            registrar_error(str(error))
            raise

    def obtener_reservas(self):

        return self.reservas