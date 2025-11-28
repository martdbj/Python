# Encapsulación, convertir métodos en atributos, decoradores
class Circulo():
    def __init__(self, radio):
        self.radio = radio

    @property
    def radio(self):
        print("Estoy dando el radio en un método con decorador")
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


# Vamos a usar un decorador @property para oonvertir un método en atributo, así podremos acceder a los métodos directamente
circ1 = Circulo(5)
print(circ1.radio)
circ1.radio = 8
print(circ1.radio)
# Borramos el atributo
del circ1.radio
print(circ1.radio)
