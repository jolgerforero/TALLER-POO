from modeloMamifero import Mamifero
from modeloReptil import Reptil
from modeloAve import Ave
from modeloInsecto import Insecto
from modeloPez import Pez

print("MAMÍFERO")
caballo = Mamifero("Caballo", 5, "Pradera", "Herbívoro", "Grande", "Café", "Pelaje corto")
caballo.mostrarInfo()

print("REPTIL")
cocodrilo = Reptil("Cocodrilo", 12, "Ríos y pantanos", "Carnívoro", "Grande", "Albino", "Escamas duras")
cocodrilo.mostrarInfo()

print("PEZ")
pezCirujano = Pez("Pez cirujano", 2, "Arrecifes", "Omnívoro", "Mediano", "Azul", "Agua salada")
pezCirujano.mostrarInfo()

print("INSECTO")
escarabajo = Insecto("Escarabajo rinoceronte", 1, "Selva", "Detritívoro", "Pequeño", "Negro", 6)
escarabajo.mostrarInfo()

print("AVE")
pato = Ave("Pato silvestre", 3, "Lagos", "Omnívoro", "Mediano", "Blanco y verde", "Pico plano")
pato.mostrarInfo()
