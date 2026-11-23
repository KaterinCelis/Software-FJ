"""Simulación de 12 operaciones. El sistema nunca se detiene por errores."""
from gestor import Gestor
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from logger import logger, RUTA_LOG


def main():
    g = Gestor()
    logger.info("=== Inicio de la simulación ===")

    print("\n1-4) Clientes")
    ana = g.registrar_cliente(nombre="Ana Pérez", documento="1052345678",
                              email="ana@mail.com", telefono="3101234567")
    luis = g.registrar_cliente(nombre="Luis Gómez", documento="79876543",
                               email="luis@mail.com", telefono="3209876543")
    g.registrar_cliente(nombre="Al", documento="123", email="malcorreo", telefono="1")  # inválido
    g.registrar_cliente(nombre="Ana Dup", documento="1052345678",
                        email="dup@mail.com", telefono="3001112233")                   # duplicado

    print("\n5-7) Servicios")
    sala = g.registrar_servicio(ReservaSala, "Sala Innovación", 50000, 25)
    equipo = g.registrar_servicio(AlquilerEquipo, "Videobeam", 20000, 2)
    asesoria = g.registrar_servicio(AsesoriaEspecializada, "Asesoría Cloud", 80000, "senior")
    g.registrar_servicio(AsesoriaEspecializada, "Asesoría X", 80000, "dios")           # inválido
    g.registrar_servicio(ReservaSala, "Sala rota", -5, 10)                             # inválido

    print("\n8-12) Reservas")
    r1 = g.crear_reserva(ana, sala, 3)
    g.crear_reserva(luis, equipo, 4)
    g.crear_reserva(ana, asesoria, 2)
    g.crear_reserva(luis, sala, 0)                  # horas inválidas
    g.crear_reserva(luis, sala, None)               # parámetro faltante
    equipo.disponible = False
    g.crear_reserva(ana, equipo, 1)                 # servicio no disponible
    g.cancelar_reserva(r1)
    g.cancelar_reserva(r1)                          # cancelar dos veces
    print("\nDemostración de métodos sobrecargados:")
    print("  simple:", asesoria.calcular_costo_simple(2),
          "| con IVA:", asesoria.calcular_costo_con_iva(2),
          "| IVA+10% desc:", asesoria.calcular_costo(2, impuesto=0.19, descuento=0.10))

    logger.info("=== Fin de la simulación (sistema estable) ===")
    print(f"\nSimulación terminada. Revisa el log en: {RUTA_LOG}")


if __name__ == "__main__":
    main()
