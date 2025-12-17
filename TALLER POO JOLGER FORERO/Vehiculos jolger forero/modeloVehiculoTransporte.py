from modeloVehiculo import Vehiculo

class VehiculoTransporte(Vehiculo):
    def __init__(self, modelo, color, motor, metodoArranque, metodoApagado, climatizacion, tipoSeguridad):
        super().__init__(modelo, color, motor, metodoArranque, metodoApagado)
        self.climatizacion = climatizacion
        self.tipoSeguridad = tipoSeguridad

    def abrirPuertaCorrediza(self):
        return "La puerta se ha abrio correctamente"

    def cerrarPuertaCorrediza(self):
        return "La puerta se cerro correctamente"

    def recogerPasajero(self, cantidad):
        return f"Se han recogido {cantidad} pasajeros"

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Climatizacion del vehiculo {self.modelo}: {self.climatizacion}")
        print(f"Tipo de seguridad del vehiculo {self.modelo}: {self.tipoSeguridad}")
