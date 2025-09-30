# Programa que pide un número entero e imprime el número de días del mes
try:    
    numeroMes = int(input("Introduce el número del mes del que deseas saber sus días: "))

    if numeroMes == 1 or numeroMes == 3 or numeroMes == 5 or numeroMes == 7 or numeroMes == 8 or numeroMes == 10 or numeroMes == 12:
        print("31")
    elif numeroMes == 4 or numeroMes == 6 or numeroMes == 9 or numeroMes == 11:
        print("30")
    else:
        print("28")
except ValueError:
    print("El número del mes debe de ser un número")