from modeloBotella import Botella
from modeloBotellaPlastico import BotellaPlastico
from modeloBotellaVidrio import BotellaVidrio

botellaNormal = Botella("Coca-Cola", "1.5L", "Especial")
botellaNormal.imprimirInfo()
print()

botellaPlastica = BotellaPlastico(
    "Pepsi", "2.5L", "Común", "Redondo", "Plástico", "Sin tinte"
)
resultadoPlastico = botellaPlastica.imprimirInfo()
print(resultadoPlastico)
print()

botellaVidrio = BotellaVidrio(
    "Kola Roman", "1.5L", "Común", "Cubo", "Vidrio", "Roja"
)
resultadoVidrio = botellaVidrio.imprimirInfo()
print(resultadoVidrio)

