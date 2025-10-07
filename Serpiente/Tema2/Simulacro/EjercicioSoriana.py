try:
    dias = ["MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]



    print("Introduce la recaudación de martes a domingo")


    counter = 0 
    recaudacion = 0
    minima_recaudacion = 0
    maxima_recaudacion = -1
    minima_dia = -1
    maxima_dia = -1

    while (counter < len(dias)):
        recaudacionDia = int(input(f"Recaudación del {dias[counter]}: "))
        
        if (recaudacionDia < minima_recaudacion):
            minima_recaudacion = recaudacionDia
            minima_dia = counter

        if (recaudacionDia > maxima_recaudacion):
            maxima_recaudacion = recaudacionDia
            maxima_dia = counter
    
        counter += 1

    print(f"Peor día {dias[minima_dia]}")  
    print(f"Mejor día {dias[maxima_dia]}")

    if (dias[maxima_dia] == "DOMINGO"):
        print("Si")
    else:
        print("No")

    
except ValueError as e:
    print(f"Error en la recaudación {e}")