# Clase abstracta Entidad y clase Cliente
from abc import ABC, abstractmethod
from excepciones import ClienteInvalidoError


class Entidad(ABC):
    # Clase abstracta: no se pueden crear objetos de ella directamente
    contador = 0

    def __init__(self):
        Entidad.contador += 1
        self._id = Entidad.contador

    def get_id(self):
        return self._id

    @abstractmethod
    def describir(self):
        pass


class Cliente(Entidad):
    def __init__(self, nombre, documento, email, telefono):
        super().__init__()
        # Atributos privados (encapsulacion). Se asignan con los set_
        # para que pasen por las validaciones
        self.__nombre = ""
        self.__documento = ""
        self.__email = ""
        self.__telefono = ""
        self.set_nombre(nombre)
        self.set_documento(documento)
        self.set_email(email)
        self.set_telefono(telefono)

    # ----- getters -----
    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento

    def get_email(self):
        return self.__email

    def get_telefono(self):
        return self.__telefono

    # ----- setters con validaciones -----
    def set_nombre(self, nombre):
        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise ClienteInvalidoError("Nombre invalido: " + str(nombre))
        self.__nombre = nombre.strip()

    def set_documento(self, documento):
        documento = str(documento)
        if not documento.isdigit() or len(documento) < 6 or len(documento) > 12:
            raise ClienteInvalidoError("Documento invalido: " + documento)
        self.__documento = documento

    def set_email(self, email):
        if not isinstance(email, str) or "@" not in email or "." not in email:
            raise ClienteInvalidoError("Email invalido: " + str(email))
        self.__email = email

    def set_telefono(self, telefono):
        telefono = str(telefono)
        if not telefono.isdigit() or len(telefono) != 10:
            raise ClienteInvalidoError("Telefono invalido: " + telefono)
        self.__telefono = telefono

    def describir(self):
        return ("Cliente #" + str(self._id) + ": " + self.__nombre +
                " (doc " + self.__documento + ", " + self.__email + ")")
