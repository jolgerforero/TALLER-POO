class Botella:
    def __init__(self, marca, capacidad, tapa):
        self.marca = marca
        self.capacidad = capacidad
        self.tapa = tapa

    def rellenarBotella(self, capacidad):
        print(f"La botella se está rellenando: {capacidad}")
        print(f"Se va a utilizar la tapa: {self.tapa}")

    def cerrarTapa(self, cantidad):
        print(f"Se utilizó la tapa: {self.tapa}")
        print(f"Cantidad de tapas utilizadas: {cantidad}")
        return cantidad

    def imprimirInfo(self):
        print(f"Marca: {self.marca}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Tipo de tapa: {self.tapa}")
