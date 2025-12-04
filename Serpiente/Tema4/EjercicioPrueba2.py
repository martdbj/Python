class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value

    def __str__(self):
        return f"{self._nombre} ({self._edad})"

    def es_mayor_edad(self):
        if self._edad >= 18:
            return True
        return False

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, value):
        self._salario = value

    def __str__(self):
        return f"{super().nombre} ({super().edad}:{self.salario})"

    def salario_anual(self):
        return self.salario * 12

persona = Persona("Miguel", 19)
empleado = Empleado("Sara", 16, 15000)

print(persona)
print(empleado)
print(persona.es_mayor_edad())
print(empleado.es_mayor_edad())
print(empleado.salario_anual())