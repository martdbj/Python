try:
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))
    resultado = num1 / num2

    print(f"El resultado es {resultado}")
except ValueError:
    print("Error: Debe ser un número")
except ZeroDivisionError:
    print("Error: No se debe dividir entre 0")
except Exception as e:
    print(f"Error inesperado. {e}")