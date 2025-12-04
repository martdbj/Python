class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Getter/Setter para x
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        self._x = valor

    # Getter/Setter para y
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, valor):
        self._y = valor

    def __str__(self):
        return "{0}:{1}".format(self.x, self.y)

    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        return (dx * dx + dy * dy) ** 0.5


class Punto3D(Punto):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    # Getter/Setter correctos para z
    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, valor):
        self._z = valor

    def __str__(self):
        return super().__str__() + ":" + str(self.z)

    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        dz = self.z - otro.z
        return (dx * dx + dy * dy + dz * dz) ** 0.5
