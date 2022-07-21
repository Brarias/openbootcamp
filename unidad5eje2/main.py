"""""En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como 
atributos su nombre y su nota. 
Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado 
de la nota y si ha aprobado o no."""""

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimirDatos(self):
        print(self.nombre)
        print(self.nota)

    def estaAprobado(self):
        if self.nota > 4:
            print("Está Aprobado")
        else:
            print("Está desaprobado")

nuevoAlumno = Alumno("Braian", 6)
nuevoAlumno.imprimirDatos()
nuevoAlumno.estaAprobado()
