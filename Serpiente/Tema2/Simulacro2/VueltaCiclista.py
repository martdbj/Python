try:
    km_totales = 0
    km_recorridos_ida = -1
    km_diaAnterior_ida = 0
    while km_recorridos_ida != 0:
        km_recorridos_ida = int(input("Escriba los kilometros recorridos este día (0 para finalizar): "))

        if km_recorridos_ida > 30:
            print("No se pueden hacer más de 60km que el día anterior")
            continue
        elif km_recorridos_ida < 0:
            print("La cantidad de km no puede ser inferior a 0")
            continue

        if km_totales == 0:
            km_totales += km_recorridos_ida
            km_diaAnterior_ida = km_totales
        elif km_recorridos_ida != 0:
            km_recorridos_ida += km_diaAnterior_ida
            km_diaAnterior_ida = km_recorridos_ida
            km_totales += km_recorridos_ida

    print(km_totales * 2)
except ValueError as e:
    print("El valor ingresado debe de ser un número")
