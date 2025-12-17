from modeloAnimales import Animal

class Pez(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, tipoAgua):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.tipoAgua = tipoAgua

    def nadar(self):
        return f"{self.nombre} esta nadando."

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Tipo de agua: {self.tipoAgua}")
        print("Reino: Pez\n")

