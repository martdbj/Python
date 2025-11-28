# Encapsulación, convertir métodos en atributos, decoradores
class Circulo():
    def __init__(self, radio):
        self.radio = radio

    @property
    def radio(self):
        return self._radio

    # Es necesario definir un setter
    @radio.setter
    def radio(self, radio):
        if radio >= 0:
            self._radio = radio
        else:
            raise ValueError("Radio debe ser positivo")

    @radio.deleter
    def radio(self):
        del self._radio

    # Podemos reescribir los métodos que nos proporciona la clase
    def __str__(self):
        clase = type(self).__name__
        msg = "{0} en mi mensaje de radio {1}"
        return msg.format(clase, self.radio)

    # Otra forma de representar un objeto para desarrollo y depurar
    def __repr__(self):
        clase = type(self).__name__
        msg = "{0}({1})"
        return msg.format(clase, self.radio)

    # Puedo reescribir el metodo para comparar objetos
    def __eq__(self, otro):
        return  self.radio == otro.radio

    # Puedo determinar como se suman circulos
    def __add__(self, otro):
        self.radio += otro.radio

# Vamos a usar un decorador @property para oonvertir un método en atributo, así podremos acceder a los métodos directamente
circ1 = Circulo(4)
print(circ1)
print(repr(circ1))

circ2 = Circulo(7)
print(circ1 == circ2)
circ1 + circ2
print(circ1)