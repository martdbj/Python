# Hay conversione explicitas e implicitas
# 1-Implicita (automática)
import math

entero = 5
decimal = 2.5

resultado = entero + decimal # Python convierte el entero a decimal
print(resultado)
print(type(resultado))

# 2- Explícito (forzado por el programa)
numero_str = "43"
numero_int = int(numero_str)
print(numero_int)

# 3- Float a entero (perdemos decimales)
print(int(math.pi))

# De entero a string
edad = 30
mensaje = "Tienes " + str(edad) + " años."
print(mensaje)

valor = True
resultado = int(valor)
print(resultado)