from modeloAnimales import Animal

class Insecto(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, numeroPatas):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.numeroPatas = numeroPatas

    def volar(self):
        return f"{self.nombre} puede volar si tiene alas."

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Numero de patas: {self.numeroPatas}")
        print("Reino: Insecto\n")
