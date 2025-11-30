# Se nombran en mayusuculas
class Clase():
    # Atributo de clase, le damos valor 1
    at_clase = 1

    # Metodo que referencia la objeto que utiliza este metodo
    def metodo(self):
        self.at_clase = 1

# Creamos un objeto de la clase
objeto = Clase()
print(type(objeto))

# Vamos a ver el valor del atributo de la clase
print(Clase.at_clase)

# Para ver el valor del atributo del objeto tengo que llamar al metodo que crea el atributo
print(objeto.at_clase)
