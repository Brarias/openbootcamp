"""
En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora:
sumar, restar, multiplicar y dividir.

Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que
mostrarlos por consola.
"""
import calculadora.suma as sum
import calculadora.resta as res
import calculadora.multiplicacion as mul
import calculadora.division as div

suma = sum.sumar(2,4)
print(suma)

resta = res.restar(8, 3)
print(resta)

multi = mul.multiplicar(5, 6)
print(multi)

divi = div.dividir(8, 4)
print(divi)

