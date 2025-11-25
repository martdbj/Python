# Ejemplo de clase con metodo estatico
class Calculadora():
    def __init__(self, nombre):
        self.nombre = nombre

    def modelo(self):
        return self.nombre

    @staticmethod
    def sumar(x, y):
        return x + y

calc1 = Calculadora("Samuel")
print("Nombre de la calculadora:", calc1.modelo())
print("Llamada al método estático sumar", Calculadora.sumar(3, 4))

# Uso de funciones
setattr(calc1, "nombre", "Jaime")
print("Nombre de la calculadora: " + getattr(calc1, "nombre"))

# Existe un atributo?
print("Hay atributo nombre?", hasattr(calc1, "nombre"))

# Borrar atributo
delattr(calc1, "nombre")
print("Hay atributo nombre?", hasattr(calc1, "nombre"))