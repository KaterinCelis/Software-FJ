""Excepciones personalizadas del sistema.""

class ErrorSistema(Exception):
    """Excepción base de Software FJ."""


class DatoInvalidoError(ErrorSistema):
    """Un dato no cumple las validaciones."""


class NoEncontradoError(ErrorSistema):
    """No se encontró el elemento solicitado."""


class OperacionNoPermitidaError(ErrorSistema):
    """La operación no está permitida."""


class ServicioNoDisponibleError(ErrorSistema):
    """El servicio no está disponible."""
