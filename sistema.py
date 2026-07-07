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
    
    def buscar_cliente(self, documento):

        documento = str(documento).strip()

        for cliente in self.clientes:

            if str(cliente.documento).strip() == documento:
                return cliente

        return None

    def modificar_cliente(self, documento, nuevos_datos):

        cliente = self.buscar_cliente(documento)

        if cliente is None:
            raise ClienteError("Cliente no encontrado.")

        cliente.nombre = nuevos_datos["nombre"]
        cliente.telefono = nuevos_datos["telefono"]
        cliente.correo = nuevos_datos["correo"]

        registrar_evento(
            f"Cliente modificado: {cliente.nombre}"
        )

    def eliminar_cliente(self, documento):

        cliente = self.buscar_cliente(documento)

        if cliente is None:
            raise ClienteError("Cliente no encontrado.")

        self.clientes.remove(cliente)

        registrar_evento(
            f"Cliente eliminado: {cliente.nombre}"
        )


    # SERVICIOS

    def agregar_servicio(self, servicio):

        try:

            for s in self.servicios:

                if s.codigo == servicio.codigo:
                    raise ServicioError(
                        "El servicio ya se encuentra registrado."
                    )

            self.servicios.append(servicio)

            registrar_evento(
                f"Servicio agregado: {servicio.nombre}"
            )

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
    