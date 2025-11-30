class Alumno():
    nombre = "Clase alumno"
    contador = 0
    def __init__(self, nombre = ""):
        self.nombre = nombre
        Alumno.contador += 1 # Atributo de clase único para todos los alumnos

alum1 = Alumno("Pepe")
alum2 = Alumno("luis")
alum3 = Alumno("Jaime")

print("¿Cuántos alumnos hay?:", Alumno.contador)
print("¿Cómo se llama?", alum1.nombre)
print("Nombre de la clase:", Alumno.nombre)