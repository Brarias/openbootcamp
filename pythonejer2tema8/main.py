"""
En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de
ella, lo guardaréis en un archivo y luego lo cargamos.
"""
import pickle
class Vehiculo:
    marca = ""
    modelo = 0

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

v1 = Vehiculo("Peugeot", 2020)
f = open('datos.bin', 'wb')
pickle.dump(v1, f)
f.close()

f2 = open('datos.bin', 'rb')
peugeot = pickle.load(f2)
print(peugeot.getMarca())
print(peugeot.getModelo())
f2.close()