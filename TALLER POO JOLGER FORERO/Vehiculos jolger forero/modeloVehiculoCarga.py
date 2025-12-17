from modeloVehiculo import Vehiculo

class VehiculoCarga(Vehiculo):
    def __init__(self, modelo, color, motor, metodoArranque, metodoApagado, climatizacion, tipoSeguridad):
        super().__init__(modelo, color, motor, metodoArranque, metodoApagado)
        self.climatizacion = climatizacion
        self.tipoSeguridad = tipoSeguridad

    def activarVolco(self):
        return "El volco se eleva para descargar la carga"

    def desactivarVolco(self):
        return "El volco vuelve a su posicion normal"

    def cargarMaterial(self, cantidad, tipo):
        return f"Se han cargado {cantidad} kg de {tipo}"

    def descargarMaterial(self):
        return "Se ha iniciado la descarga del material"

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Climatizacion: {self.climatizacion}")
        print(f"Tipo de seguridad: {self.tipoSeguridad}")
        return "Informacion adquirida exitosamente"
