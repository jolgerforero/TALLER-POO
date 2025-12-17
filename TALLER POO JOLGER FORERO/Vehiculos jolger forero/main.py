from modeloVehiculoDeportivo import VehiculoDeportivo
from modeloVehiculoTransporte import VehiculoTransporte
from modeloVehiculoCarga import VehiculoCarga

print("VEHICULO DEPORTIVO")
vehiculoDeportivo = VehiculoDeportivo(
    "BMW Z4 Roadster",
    "Gris metalico",
    "3.0L TwinPower Turbo",
    """
- Boton de encendido
- Llave inteligente
- Llave de proximidad
""",
    """
- Boton Start Stop
- Apagado automatico
""",
    "Climatizador bizona automatico",
    """
- Llave inteligente
- Control remoto
"""
)
vehiculoDeportivo.mostrarInfo()
print("--------------------------------")

print("VEHICULO TRANSPORTE")
vehiculoTransporte = VehiculoTransporte(
    "JAC Sunray Passenger Van",
    "Blanco polar",
    "Motor 2.0L Turbo Diesel",
    """
- Llave tradicional
- Encendido por giro
""",
    """
- Giro manual
""",
    "Aire acondicionado completo",
    """
- Cierre centralizado
- Alarma
"""
)
vehiculoTransporte.mostrarInfo()
print("--------------------------------")

print("VEHICULO CARGA")
vehiculoCarga = VehiculoCarga(
    "JAC Heavy Duty Truck",
    "Blanco estandar",
    "Motor 3.8L Turbo Diesel",
    """
- Llave reforzada
- Encendido por giro
""",
    """
- Apagado manual
""",
    "Aire acondicionado basico",
    """
- Seguros reforzados
- Barra antirrobo
"""
)
vehiculoCarga.mostrarInfo()



