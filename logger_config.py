# Importa la libreria logging
import logging

# Configuracion del archivo de logs
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Registrar informacion
def registrar_evento(mensaje):

    logging.info(mensaje)

# Registrar errores
def registrar_error(mensaje):

    logging.error(mensaje)