# Clase Reserva: une un cliente, un servicio, las horas y el estado
from entidades import Entidad, Cliente
from servicios import Servicio
from excepciones import (ReservaInvalidaError, OperacionNoPermitidaError,
                         ErrorSoftwareFJ)
import logger


class Reserva(Entidad):
    def __init__(self, cliente, servicio, horas):
        super().__init__()
        if not isinstance(cliente, Cliente) or not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("Cliente o servicio invalido")
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "PENDIENTE"
        self.costo = None

    def confirmar(self):
        if self.estado != "PENDIENTE":
            raise OperacionNoPermitidaError(
                "No se puede confirmar una reserva " + self.estado)
        try:
            self.costo = self.servicio.calcular_costo_con_iva(self.horas)
        except ErrorSoftwareFJ as e:
            # Encadenamiento de excepciones: "from e" guarda el error original
            raise ReservaInvalidaError("No se pudo confirmar la reserva") from e
        else:
            self.estado = "CONFIRMADA"
            logger.info("Reserva #" + str(self._id) + " confirmada. Total $" + str(self.costo))
        finally:
            logger.info("Termino el intento de confirmar la reserva #" + str(self._id))

    def cancelar(self):
        if self.estado == "CANCELADA":
            raise OperacionNoPermitidaError("La reserva ya estaba cancelada")
        self.estado = "CANCELADA"
        logger.info("Reserva #" + str(self._id) + " cancelada")

    def describir(self):
        return ("Reserva #" + str(self._id) + " | " + self.cliente.get_nombre() +
                " | " + self.servicio.get_nombre() + " | " + str(self.horas) +
                "h | " + self.estado + " | $" + str(self.costo))
