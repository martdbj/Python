try:
    num = int(input("Introduce un número: "))

except ValueError:
    print("Entrada invállida, debe se un número")
except Exception as e:
    print(e)
else:
    print(f"El número introducido es: {num}")
    print("No se ha producido una excepción")