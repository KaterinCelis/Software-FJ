"""Gestor en memoria (listas internas, sin base de datos)."""
from entidades import Cliente
from reserva import Reserva
from excepciones import ErrorSoftwareFJ, ClienteInvalidoError
from logger import logger


class Gestor:
    def __init__(self):
        self._clientes, self._servicios, self._reservas = [], [], []

    def registrar_cliente(self, **datos):
        try:
            c = Cliente(**datos)
            if any(x.documento == c.documento for x in self._clientes):
                raise ClienteInvalidoError("Documento ya registrado")
        except (ErrorSoftwareFJ, TypeError) as e:
            logger.error(f"Registro de cliente fallido: {e!r}")
            print(f"  [ERROR] Cliente: {e}")
            return None
        else:
            self._clientes.append(c)
            logger.info(f"Cliente registrado: {c.describir()}")
            print(f"  [OK] {c.describir()}")
            return c

    def registrar_servicio(self, clase, *args, **kwargs):
        try:
            s = clase(*args, **kwargs)
        except (ErrorSoftwareFJ, TypeError) as e:
            logger.error(f"Creación de servicio fallida: {e!r}")
            print(f"  [ERROR] Servicio: {e}")
            return None
        else:
            self._servicios.append(s)
            logger.info(f"Servicio creado: {s.describir()}")
            print(f"  [OK] {s.describir()}")
            return s

    def crear_reserva(self, cliente, servicio, horas, confirmar=True):
        try:
            if servicio is None or cliente is None:
                raise ErrorSoftwareFJ("Cliente o servicio inexistente")
            servicio.validar_parametros(horas)
            r = Reserva(cliente, servicio, horas)
            if confirmar:
                r.confirmar()
            self._reservas.append(r)
        except ErrorSoftwareFJ as e:
            causa = f" (causa: {e.__cause__})" if e.__cause__ else ""
            logger.error(f"Reserva fallida: {e!r}{causa}")
            print(f"  [ERROR] Reserva: {e}{causa}")
            return None
        else:
            print(f"  [OK] {r.describir()}")
            return r
        finally:
            logger.info("Operación de reserva procesada")

    def cancelar_reserva(self, reserva):
        try:
            reserva.cancelar()
            print(f"  [OK] {reserva.describir()}")
        except (ErrorSoftwareFJ, AttributeError) as e:
            logger.error(f"Cancelación fallida: {e!r}")
            print(f"  [ERROR] Cancelación: {e}")
