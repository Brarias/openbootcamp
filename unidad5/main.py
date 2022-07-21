""" En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

Color

Ruedas

Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

Velocidad

Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola."""

class Vehiculo:
    color = "Azul"
    ruedas = 4
    puertas = 2

class Coche(Vehiculo):
    velocidad = 100
    cilindrada = 2.0


miCoche = Coche()
print(miCoche.cilindrada)
print(miCoche.color)
print(miCoche.velocidad)
print(miCoche.ruedas)
print(miCoche.puertas)