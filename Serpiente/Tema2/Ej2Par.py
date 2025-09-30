# Programa que lee un número y musetra si es par o impar

try:
    userNumber = int(input("Inserte un número para comprobar si es par o impar: "))

    if userNumber % 2 == 0:
        print("El número ", userNumber, " es par")
    else:
        print("El número ", userNumber, " es impar")

except ValueError:
    print("Debes de insertar un número válido")

