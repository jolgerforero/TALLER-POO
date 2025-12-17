from modeloAnimales import Animal

class Ave(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, tipoPico):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.tipoPico = tipoPico

    def volar(self):
        return f"{self.nombre} esta volando."

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Tipo de pico: {self.tipoPico}")
        print("Reino: Ave\n")
