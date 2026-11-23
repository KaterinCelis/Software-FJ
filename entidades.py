"""Clase abstracta Entidad y clase Cliente (encapsulación + validaciones)."""
import re
from abc import ABC, abstractmethod
from excepciones import ClienteInvalidoError


class Entidad(ABC):
    """Entidad general del sistema."""
    _contador = 0

    def __init__(self):
        Entidad._contador += 1
        self._id = Entidad._contador

    @property
    def id(self):
        return self._id

    @abstractmethod
    def describir(self) -> str:
        ...


class Cliente(Entidad):
    def __init__(self, nombre, documento, email, telefono):
        super().__init__()
        self.nombre = nombre          # pasan por los setters validados
        self.documento = documento
        self.email = email
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, v):
        if not isinstance(v, str) or len(v.strip()) < 3:
            raise ClienteInvalidoError(f"Nombre inválido: {v!r}")
        self.__nombre = v.strip()

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, v):
        if not str(v).isdigit() or not 6 <= len(str(v)) <= 12:
            raise ClienteInvalidoError(f"Documento inválido: {v!r}")
        self.__documento = str(v)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, v):
        if not isinstance(v, str) or not re.fullmatch(r"[\w.+-]+@[\w-]+\.[\w.]+", v):
            raise ClienteInvalidoError(f"Email inválido: {v!r}")
        self.__email = v

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, v):
        if not str(v).isdigit() or len(str(v)) != 10:
            raise ClienteInvalidoError(f"Teléfono inválido: {v!r}")
        self.__telefono = str(v)

    def describir(self):
        return f"Cliente #{self.id}: {self.nombre} (doc {self.documento}, {self.email})"
