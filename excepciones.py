# Excepcion para clientes invalidos
class ClienteError(Exception):
    pass

# Excepcion para servicios invalidos
class ServicioError(Exception):
    pass

# Excepcion para reservas invalidos
class ReservaError(Exception):
    pass

# Excepcion para datos invalidos
class ValidacionError(Exception):
    pass