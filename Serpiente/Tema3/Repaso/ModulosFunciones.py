# Práctica módulos y funciones

# OperacionesAvanzadas.py
PI = 3.14159

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def calcular_area_circulo(radio):
    return PI * (radio ** 2)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b