from modeloVehiculo import Vehiculo

class VehiculoDeportivo(Vehiculo):
    def __init__(self, modelo, color, motor, metodoArranque, metodoApagado, climatizacion, tipoSeguridad):
        super().__init__(modelo, color, motor, metodoArranque, metodoApagado)
        self.climatizacion = climatizacion
        self.tipoSeguridad = tipoSeguridad

    def activarModoSport(self):
        return "El modo sport se ha activado. La respuesta del motor aumenta"

    def abrirCapota(self):
        return "La capota del deportivo se abre automaticamente"

    def cerrarCapota(self):
        return "La capota del deportivo se cierra"

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Climatizacion: {self.climatizacion}")
        print(f"Tipo de seguridad: {self.tipoSeguridad}")
        return "Informacion adquirida exitosamente"
