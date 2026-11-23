# Excepciones personalizadas del sistema

class ErrorSoftwareFJ(Exception):
    # Esta es la excepcion "padre" de todas las demas
    pass

class ClienteInvalidoError(ErrorSoftwareFJ):
    pass

class ParametroFaltanteError(ErrorSoftwareFJ):
    pass

class ServicioNoDisponibleError(ErrorSoftwareFJ):
    pass

class OperacionNoPermitidaError(ErrorSoftwareFJ):
    pass

class ReservaInvalidaError(ErrorSoftwareFJ):
    pass

class CalculoInconsistenteError(ErrorSoftwareFJ):
    pass
