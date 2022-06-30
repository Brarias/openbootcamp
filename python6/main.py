#Escribe una función que pueda decirte si un número (número entero) es primo o no.

def esPrimo(numero):
    cont = 0
    for valor in range(2, numero):
        resto = numero % valor
        if resto == 0:
            cont += 1

    if cont == 0:
      print("Es primo")
    else:
      print("No es primo")





esPrimo(1009)
