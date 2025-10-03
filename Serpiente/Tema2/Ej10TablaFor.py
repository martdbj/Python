# Pedir un número por pantall y mostrar la tabla de multiplicar

try:
    numero = int(input("Introduzca un número: "))
    print("Tabla con for")
    for i in range(1, 11):
        print(numero, " * ", i, " = ", numero * i)

    print("\nTabla con while")
    i = 1
    while i < 11:
        print(numero, " * ", i, " = ", numero * i)
        i += 1
except ValueError:
    print("El valor introducido debe de ser un número")