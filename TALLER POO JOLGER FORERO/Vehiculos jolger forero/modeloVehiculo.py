class Vehiculo:
    def __init__(self, modelo, color, motor, metodoArranque, metodoApagado):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.metodoArranque = metodoArranque
        self.metodoApagado = metodoApagado

    def aceleracion(self):
        return "El vehiculo acelera de forma gradual"

    def frenado(self):
        return "El vehiculo decrementa su velocidad de forma gradual"

    def mostrarInfo(self):
        print(f"Modelo del vehiculo: {self.modelo}")
        print(f"Color del vehiculo: {self.color}")
        print(f"Motor del vehiculo: {self.motor}")
        print(f"Metodo de arranque: {self.metodoArranque}")
        print(f"Metodo de apagado: {self.metodoApagado}")
