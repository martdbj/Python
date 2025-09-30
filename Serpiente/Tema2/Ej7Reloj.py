# Si el reloj marca las 03:15, serían las 20:45
try:
    hora = int(input("Introduce la hora (1-12): "))
    minutos = int(input("Introduce los minutos (0-59): "))

    horaFinal = 0
    minutosFinal = 0
    
    if minutos == 0:
        horaFinal = 24 - hora
    else:
        horaFinal = 24 - (hora + 1)
        minutosFinal = 60 - minutos

    print("La hora real es ", horaFinal, ":", minutosFinal)
except ValueError:
    print("La hora y los minutos deben de ser numéricos")