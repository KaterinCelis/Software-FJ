# Clase abstracta Servicio y tres servicios que heredan de ella
from abc import abstractmethod
from entidades import Entidad
from excepciones import (ParametroFaltanteError, ServicioNoDisponibleError,
                         CalculoInconsistenteError)

IVA = 0.19


class Servicio(Entidad):
    def __init__(self, nombre, tarifa_hora):
        super().__init__()
        if nombre is None or nombre == "" or tarifa_hora is None:
            raise ParametroFaltanteError("El servicio necesita nombre y tarifa")
        if tarifa_hora <= 0:
            raise CalculoInconsistenteError("La tarifa debe ser positiva")
        self._nombre = nombre
        self._tarifa_hora = tarifa_hora
        self._disponible = True

    def get_nombre(self):
        return self._nombre

    def set_disponible(self, valor):
        self._disponible = valor

    def validar_parametros(self, horas):
        if horas is None:
            raise ParametroFaltanteError("Falta la duracion (horas)")
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ParametroFaltanteError("Duracion invalida: " + str(horas))
        if not self._disponible:
            raise ServicioNoDisponibleError(self._nombre + " no esta disponible")

    @abstractmethod
    def costo_base(self, horas):
        pass

    # Metodo "sobrecargado": en Python se hace con parametros opcionales
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        self.validar_parametros(horas)
        if descuento < 0 or descuento >= 1 or impuesto < 0:
            raise CalculoInconsistenteError("Impuesto o descuento fuera de rango")
        total = self.costo_base(horas) * (1 - descuento) * (1 + impuesto)
        if total <= 0:
            raise CalculoInconsistenteError("El costo calculado no es valido")
        return round(total, 2)

    # Otras versiones del calculo
    def calcular_costo_simple(self, horas):
        return self.calcular_costo(horas)

    def calcular_costo_con_iva(self, horas, descuento=0):
        return self.calcular_costo(horas, IVA, descuento)

    @abstractmethod
    def describir(self):
        pass


class ReservaSala(Servicio):
    def __init__(self, nombre, tarifa_hora, capacidad):
        super().__init__(nombre, tarifa_hora)
        self._capacidad = capacidad

    def costo_base(self, horas):
        total = self._tarifa_hora * horas
        if self._capacidad > 20:
            total = total * 1.10   # recargo por sala grande
        return total

    def describir(self):
        return ("Sala '" + self._nombre + "' (capacidad " + str(self._capacidad) +
                ") $" + str(self._tarifa_hora) + "/h")


class AlquilerEquipo(Servicio):
    def __init__(self, nombre, tarifa_hora, cantidad=1, seguro=15000):
        super().__init__(nombre, tarifa_hora)
        self._cantidad = cantidad
        self._seguro = seguro

    # Metodo sobrescrito: hace lo del padre y agrega una validacion
    def validar_parametros(self, horas):
        super().validar_parametros(horas)
        if self._cantidad < 1:
            raise ParametroFaltanteError("Cantidad de equipos invalida")

    def costo_base(self, horas):
        return self._tarifa_hora * horas * self._cantidad + self._seguro

    def describir(self):
        return ("Equipo '" + self._nombre + "' x" + str(self._cantidad) +
                " $" + str(self._tarifa_hora) + "/h + seguro")


class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre, tarifa_hora, nivel="junior"):
        super().__init__(nombre, tarifa_hora)
        if nivel != "junior" and nivel != "senior" and nivel != "experto":
            raise ParametroFaltanteError("Nivel de asesor invalido: " + str(nivel))
        self._nivel = nivel

    def costo_base(self, horas):
        total = self._tarifa_hora * horas
        if self._nivel == "senior":
            total = total * 1.6
        elif self._nivel == "experto":
            total = total * 2.2
        return total

    def describir(self):
        return ("Asesoria '" + self._nombre + "' nivel " + self._nivel +
                " $" + str(self._tarifa_hora) + "/h")
