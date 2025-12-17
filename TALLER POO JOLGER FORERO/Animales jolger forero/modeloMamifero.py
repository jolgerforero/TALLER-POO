from modeloAnimales import Animal

class Mamifero(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, tipoPelo):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.tipoPelo = tipoPelo

    def amamantar(self):
        return f"{self.nombre} amamanta a sus crias."

    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Tipo de pelo: {self.tipoPelo}")
        print("Reino: Mamífero\n")

