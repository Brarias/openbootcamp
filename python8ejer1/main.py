"""
En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del
archivo. Para ello, tendréis que acceder dos veces al archivo creado.
"""

f = open('datos.txt', 'w')
datos = [
    'Aquí me pongo a cantar\n',
    'al compás de la vigüela,\n',
    'que al hombre que lo desvela\n',
    'una pena estraordinaria\n',
    'como la ave solitaria\n',
    'con el cantar se consuela'
]
f.writelines(datos)
f.close()

f2 = open('datos.txt', 'r')
datosLeer = f2.readlines()
for linea in datosLeer:
    print(linea)
f2.close()

