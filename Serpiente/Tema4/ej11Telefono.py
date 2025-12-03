class Telefono():
    def __init__(self, numero):
        self.numero = numero

    def telefonear(self):
        return "Telefonear"

    def colgar(self):
        return "Colgar"

    def __str__(self):
        return self.numero

class Camara():
    def __init__(self, mpx):
        self.mpx = mpx

    def fotografiar(self):
        return "Fotografiando"

    def __str__(self):
        return self.mpx

class Reproductor():
    def __init__(self, capacidad):
        self.capacidad = capacidad

    def reproducirVideo(self):
        return "Reproduciendo Vídeo"

    def reproducirMP3(self):
        return "Reproduciendo mp3"

    def __str__(self):
        return self.capacidad

class Movil(Telefono, Camara,  Reproductor):
    def __init__(self, numero=0, mpx=0, capacidad=0):
        super().__init__(numero
        self.numero = Telefono(numero)
        self.mpx = Camara(mpx)
        self.capacidad = Reproductor(capacidad)

    def __str__(self):
        return "Número {0} \n Cámara {1} \n Capacidad {2}".format(self.numero, self.mpx, self.capacidad)



