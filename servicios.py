"""Clase abstracta Servicio y tres servicios especializados (polimorfismo)."""
from abc import abstractmethod
from entidades import Entidad
from excepciones import (ParametroFaltanteError, ServicioNoDisponibleError,
                         CalculoInconsistenteError)

IVA = 0.19


class Servicio(Entidad):
    def __init__(self, nombre, tarifa_hora):
        super().__init__()
        if not nombre or tarifa_hora is None:
            raise ParametroFaltanteError("Servicio requiere nombre y tarifa")
        if tarifa_hora <= 0:
            raise CalculoInconsistenteError("La tarifa debe ser positiva")
        self._nombre = nombre
        self._tarifa_hora = tarifa_hora
        self._disponible = True

    @property
    def nombre(self):
        return self._nombre

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        self._disponible = bool(valor)

    def validar_parametros(self, horas):
        if horas is None:
            raise ParametroFaltanteError("Falta la duración (horas)")
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ParametroFaltanteError(f"Duración inválida: {horas!r}")
        if not self._disponible:
            raise ServicioNoDisponibleError(f"'{self._nombre}' no está disponible")

    @abstractmethod
    def costo_base(self, horas) -> float:
        """Costo sin impuestos ni descuentos (cada servicio lo define)."""

    # --- Método "sobrecargado": parámetros opcionales (impuesto / descuento) ---
    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        self.validar_parametros(horas)
        if not 0 <= descuento < 1 or impuesto < 0:
            raise CalculoInconsistenteError("Impuesto o descuento fuera de rango")
        total = self.costo_base(horas) * (1 - descuento) * (1 + impuesto)
        if total <= 0:
            raise CalculoInconsistenteError("Costo calculado no válido")
        return round(total, 2)

    def calcular_costo_con_iva(self, horas, descuento=0.0):
        """Variante: aplica IVA fijo."""
        return self.calcular_costo(horas, impuesto=IVA, descuento=descuento)

    def calcular_costo_simple(self, horas):
        """Variante: solo costo base."""
        return self.calcular_costo(horas)

    @abstractmethod
    def describir(self) -> str:
        ...


class ReservaSala(Servicio):
    def __init__(self, nombre, tarifa_hora, capacidad):
        super().__init__(nombre, tarifa_hora)
        self._capacidad = capacidad

    def costo_base(self, horas):
        recargo = 1.10 if self._capacidad > 20 else 1.0
        return self._tarifa_hora * horas * recargo

    def describir(self):
        return f"Sala '{self._nombre}' (capacidad {self._capacidad}) ${self._tarifa_hora}/h"


class AlquilerEquipo(Servicio):
    def __init__(self, nombre, tarifa_hora, cantidad=1, seguro=15000):
        super().__init__(nombre, tarifa_hora)
        self._cantidad = cantidad
        self._seguro = seguro

    def validar_parametros(self, horas):
        super().validar_parametros(horas)          # método sobrescrito
        if self._cantidad < 1:
            raise ParametroFaltanteError("Cantidad de equipos inválida")

    def costo_base(self, horas):
        return self._tarifa_hora * horas * self._cantidad + self._seguro

    def describir(self):
        return f"Equipo '{self._nombre}' x{self._cantidad} ${self._tarifa_hora}/h + seguro"


class AsesoriaEspecializada(Servicio):
    NIVELES = {"junior": 1.0, "senior": 1.6, "experto": 2.2}

    def __init__(self, nombre, tarifa_hora, nivel="junior"):
        super().__init__(nombre, tarifa_hora)
        if nivel not in self.NIVELES:
            raise ParametroFaltanteError(f"Nivel de asesor inválido: {nivel!r}")
        self._nivel = nivel

    def costo_base(self, horas):
        return self._tarifa_hora * horas * self.NIVELES[self._nivel]

    def describir(self):
        return f"Asesoría '{self._nombre}' nivel {self._nivel} ${self._tarifa_hora}/h"
