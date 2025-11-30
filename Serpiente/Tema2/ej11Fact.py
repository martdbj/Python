# Aplicación que pide un número y calcula el factorial 

try:
    numero = int(input("Escribe un número para calcular su factorial: "))
    factorial = 1
    for i in range(2, numero + 1):
        factorial *= i
    print("El factorial de", numero, "es", factorial)
except ValueError:
    print("El valor introducido debe de ser un número")