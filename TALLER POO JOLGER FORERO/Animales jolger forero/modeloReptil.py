from modeloAnimales import Animal

class Reptil(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, tipoEscamas):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.tipoEscamas = tipoEscamas

    def regularTemperatura(self):
        return f"{self.nombre} toma el sol para regular su temperatura."

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Tipo de escamas: {self.tipoEscamas}")
        print("Reino: Reptil\n")

