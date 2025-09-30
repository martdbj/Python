# Programa que pide dos números enteros y dice si la suma es positiva, negativo o 0
try:
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el segundo número: "))

    suma = numero1 + numero2

    if (suma > 0):
        print("La suma es positiva")
    elif (suma < 0):
        print("La suma es negativa")
    else:
        print("La suma es 0")
        
except ValueError:
    print("Tienes que insertar un número. Error")