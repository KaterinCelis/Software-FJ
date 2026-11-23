"""Excepciones personalizadas de Software FJ."""


class ErrorSoftwareFJ(Exception):
    """Excepción base del sistema."""


class ClienteInvalidoError(ErrorSoftwareFJ):
    """Datos de cliente inválidos."""


class ParametroFaltanteError(ErrorSoftwareFJ):
    """Falta un parámetro obligatorio."""


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """El servicio no está disponible."""


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """Operación no permitida por el estado actual."""


class ReservaInvalidaError(ErrorSoftwareFJ):
    """La reserva no se pudo crear o procesar."""


class CalculoInconsistenteError(ErrorSoftwareFJ):
    """Un cálculo dio un resultado inconsistente."""
