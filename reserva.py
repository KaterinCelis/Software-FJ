"""Clase Reserva: integra cliente, servicio, duración y estado."""
from entidades import Entidad, Cliente
from servicios import Servicio
from excepciones import (ReservaInvalidaError, OperacionNoPermitidaError,
                         ErrorSoftwareFJ)
from logger import logger


class Reserva(Entidad):
    PENDIENTE, CONFIRMADA, CANCELADA = "PENDIENTE", "CONFIRMADA", "CANCELADA"

    def __init__(self, cliente, servicio, horas):
        super().__init__()
        if not isinstance(cliente, Cliente) or not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("Cliente o servicio inválido")
        self.cliente, self.servicio, self.horas = cliente, servicio, horas
        self.estado = self.PENDIENTE
        self.costo = None

    def confirmar(self):
        if self.estado != self.PENDIENTE:
            raise OperacionNoPermitidaError(
                f"No se puede confirmar una reserva {self.estado}")
        try:
            self.costo = self.servicio.calcular_costo_con_iva(self.horas)
        except ErrorSoftwareFJ as e:
            # encadenamiento de excepciones
            raise ReservaInvalidaError("No se pudo confirmar la reserva") from e
        else:
            self.estado = self.CONFIRMADA
            logger.info(f"Reserva #{self.id} confirmada. Total ${self.costo}")
        finally:
            logger.info(f"Intento de confirmación de reserva #{self.id} finalizado")

    def cancelar(self):
        if self.estado == self.CANCELADA:
            raise OperacionNoPermitidaError("La reserva ya estaba cancelada")
        self.estado = self.CANCELADA
        logger.info(f"Reserva #{self.id} cancelada")

    def describir(self):
        return (f"Reserva #{self.id} | {self.cliente.nombre} | "
                f"{self.servicio.nombre} | {self.horas}h | {self.estado} | ${self.costo}")
