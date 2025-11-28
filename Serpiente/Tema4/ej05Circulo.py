class Circulo():
    def __init__(self, radio):
        self.set_radio(radio)

    def set_radio(self, radio):
        if radio >= 0:
            self._radio = radio
        else:
            self._radio = 0
            raise ValueError("El radio debe ser positivo")

    def get_radio(self):
        print("Estoy devolviendo el radio")
        return self._radio

circ1 = Circulo(10)
print(circ1.get_radio())