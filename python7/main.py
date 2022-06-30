#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def esBisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0:
        return True
    elif anio % 100 == 0 and anio % 400 == 0:
        return True
    else:
        return False



print(esBisiesto(2000))