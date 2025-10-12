try:
    km_totales_ida = 0
    km_recorridos = -1
    km_diaAnterior = 0
    while (True):
        km_recorridos = int(
            input("Introduce el número de km recorridos (Introduce 0 para terminar): "))
        
        if km_recorridos > 30:
            raise ValueError("Los kilometros recorridos no pueden ser más de 30")
        if km_recorridos < 0:
            raise ValueError("Los kilometros no pueden ser menores de 0")
        if km_recorridos == 0:
            break
        elif km_totales_ida == 0:
            km_totales_ida += km_recorridos
            km_diaAnterior += km_recorridos
        elif km_totales_ida != 0:
            km_recorridos += km_diaAnterior
            km_diaAnterior = km_recorridos
            km_totales_ida += km_recorridos
    km_totales = km_totales_ida * 2
    print(f"El número de km totales recorridos es de: {km_totales}")
except ValueError as e:
    print(e)
