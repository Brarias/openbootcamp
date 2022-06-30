#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y
# otra función que calcule el área de un círculo recibiendo el radio del mismo.

def areaTriangulo(base, altura):
    return (base* altura) / 2


def areaCirculo(radio):
    PI = 3.14
    return PI*(radio ** 2)

resultado = areaCirculo(4)
print(resultado)