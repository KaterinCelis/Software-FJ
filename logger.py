# Aqui se guardan los eventos y errores en un archivo de texto
import os
from datetime import datetime

RUTA_LOG = "logs/eventos.log"

# Si la carpeta logs no existe, la creamos
if not os.path.exists("logs"):
    os.makedirs("logs")


def limpiar_log():
    archivo = open(RUTA_LOG, "w", encoding="utf-8")
    archivo.close()


def registrar(nivel, mensaje):
    archivo = open(RUTA_LOG, "a", encoding="utf-8")
    archivo.write(str(datetime.now()) + " | " + nivel + " | " + mensaje + "\n")
    archivo.close()


def info(mensaje):
    registrar("INFO", mensaje)


def error(mensaje):
    registrar("ERROR", mensaje)
