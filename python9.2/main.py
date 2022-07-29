"""
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por
parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
"""
from functools import reduce
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def numerosImpares(x):
    retorno = False
    if not x % 2 == 0:
        retorno = True

    return retorno

def suma(a, b):
    
    return a + b



resultado = filter(numerosImpares, numeros)
resultado_dos = reduce(suma, resultado)
print(resultado_dos)