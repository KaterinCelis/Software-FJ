# Programa principal: simula 12 operaciones (con y sin errores)
from gestor import Gestor
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
import logger


def main():
    logger.limpiar_log()
    gestor = Gestor()
    logger.info("=== Inicio de la simulacion ===")

    print("\n1-4) Clientes")
    ana = gestor.registrar_cliente("Ana Perez", "1052345678", "ana@mail.com", "3101234567")
    luis = gestor.registrar_cliente("Luis Gomez", "79876543", "luis@mail.com", "3209876543")
    gestor.registrar_cliente("Al", "123", "malcorreo", "1")                       # datos invalidos
    gestor.registrar_cliente("Ana Dup", "1052345678", "dup@mail.com", "3001112233")  # documento repetido

    print("\n5-7) Servicios")
    sala = gestor.registrar_servicio(ReservaSala, "Sala Innovacion", 50000, 25)
    equipo = gestor.registrar_servicio(AlquilerEquipo, "Videobeam", 20000, 2)
    asesoria = gestor.registrar_servicio(AsesoriaEspecializada, "Asesoria Cloud", 80000, "senior")
    gestor.registrar_servicio(AsesoriaEspecializada, "Asesoria X", 80000, "dios")  # nivel invalido
    gestor.registrar_servicio(ReservaSala, "Sala rota", -5, 10)                    # tarifa negativa

    print("\n8-12) Reservas")
    reserva1 = gestor.crear_reserva(ana, sala, 3)
    gestor.crear_reserva(luis, equipo, 4)
    gestor.crear_reserva(ana, asesoria, 2)
    gestor.crear_reserva(luis, sala, 0)       # horas invalidas
    gestor.crear_reserva(luis, sala, None)    # falta parametro
    equipo.set_disponible(False)
    gestor.crear_reserva(ana, equipo, 1)      # servicio no disponible
    gestor.cancelar_reserva(reserva1)
    gestor.cancelar_reserva(reserva1)         # ya estaba cancelada

    print("\nDemostracion de metodos sobrecargados:")
    print("  simple:", asesoria.calcular_costo_simple(2))
    print("  con IVA:", asesoria.calcular_costo_con_iva(2))
    print("  IVA + 10% descuento:", asesoria.calcular_costo(2, 0.19, 0.10))

    logger.info("=== Fin de la simulacion ===")
    print("\nSimulacion terminada. Revisa el archivo logs/eventos.log")


main()
