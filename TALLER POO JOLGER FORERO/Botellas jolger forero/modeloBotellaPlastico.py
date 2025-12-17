from modeloBotella import Botella

class BotellaPlastico(Botella):
    def __init__(self, marca, capacidad, tapa, diseno, material, color):
        super().__init__(marca, capacidad, tapa)
        self.diseno = diseno
        self.material = material
        self.color = color

    def reciclarBotella(self):
        print(f"La botella se reciclará. Material: {self.material}")

    def imprimirInfo(self):
        super().imprimirInfo()
        print(f"Diseño: {self.diseno}")
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        return "Información encontrada exitosamente"
