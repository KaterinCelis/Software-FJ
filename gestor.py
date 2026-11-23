# Gestor: guarda todo en listas (no usamos base de datos)
from entidades import Cliente
from reserva import Reserva
from excepciones import ErrorSoftwareFJ, ClienteInvalidoError
import logger


class Gestor:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, nombre, documento, email, telefono):
        try:
            cliente = Cliente(nombre, documento, email, telefono)
            # revisar que el documento no este repetido
            for c in self.clientes:
                if c.get_documento() == cliente.get_documento():
                    raise ClienteInvalidoError("Documento ya registrado")
        except ErrorSoftwareFJ as e:
            logger.error("Registro de cliente fallido: " + str(e))
            print("  [ERROR] Cliente: " + str(e))
            return None
        else:
            self.clientes.append(cliente)
            logger.info("Cliente registrado: " + cliente.describir())
            print("  [OK] " + cliente.describir())
            return cliente

    def registrar_servicio(self, clase, *datos):
        try:
            servicio = clase(*datos)
        except ErrorSoftwareFJ as e:
            logger.error("Creacion de servicio fallida: " + str(e))
            print("  [ERROR] Servicio: " + str(e))
            return None
        else:
            self.servicios.append(servicio)
            logger.info("Servicio creado: " + servicio.describir())
            print("  [OK] " + servicio.describir())
            return servicio

    def crear_reserva(self, cliente, servicio, horas):
        try:
            if cliente is None or servicio is None:
                raise ErrorSoftwareFJ("Cliente o servicio inexistente")
            servicio.validar_parametros(horas)
            reserva = Reserva(cliente, servicio, horas)
            reserva.confirmar()
            self.reservas.append(reserva)
        except ErrorSoftwareFJ as e:
            mensaje = str(e)
            if e.__cause__ is not None:
                mensaje = mensaje + " (causa: " + str(e.__cause__) + ")"
            logger.error("Reserva fallida: " + mensaje)
            print("  [ERROR] Reserva: " + mensaje)
            return None
        else:
            print("  [OK] " + reserva.describir())
            return reserva
        finally:
            logger.info("Se proceso un intento de reserva")

    def cancelar_reserva(self, reserva):
        try:
            reserva.cancelar()
            print("  [OK] " + reserva.describir())
        except ErrorSoftwareFJ as e:
            logger.error("Cancelacion fallida: " + str(e))
            print("  [ERROR] Cancelacion: " + str(e))
