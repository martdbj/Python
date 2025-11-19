"""Representación de un punto en el plano, atributos x, y
   Los metodos especiales empiezan  teminan con __
   Los atributos de objeto se inicializan en el constructor llamado __init__"""
import math
class Punto():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def mostrar(self):
        print(self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distancia(self, otro):
        dx = otro.get_x() - self.get_x()
        dy = otro.get_y() - self.get_y()
        return math.sqrt(dx**2 + dy**2)


punto1 = Punto(3, 4)
punto2 = Punto(7, 1)

punto1.mostrar()
punto2.mostrar()

print(punto2.distancia(punto1))