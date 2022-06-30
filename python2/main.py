# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

numeroInicial = int(input("Ingrese un número inicial: "))
numeroFinal =  int(input("Ingrese un número final: "))
numerosImpares = []

while numeroInicial <= numeroFinal:
    if numeroInicial % 2 != 0:
        numerosImpares.append(numeroInicial)

    numeroInicial += 1

print(numerosImpares)

