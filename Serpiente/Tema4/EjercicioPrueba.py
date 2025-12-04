class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @property # Getter
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    def __str__(self):
        return f"{self.marca}:{self.modelo}"

    def velocidad_maxima(self):
        return 100

class Coche(Vehiculo):
    def __init__(self, marca, modelo, caballos):
        super().__init__(marca, modelo)
        self.caballos = caballos

    @property
    def caballos(self):
        return self._caballos

    @caballos.setter
    def caballos(self, value):
        self._caballos = value

    def velocidad_maxima(self):
        return super().velocidad_maxima() * self.caballos


coche1 = Coche("Toyota", "Yaris", 20)
print(coche1)
print(coche1.velocidad_maxima())
