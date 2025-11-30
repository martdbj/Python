def sumar(n1, n2, *, op = "+"):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    else:
        return "error"
    
print(sumar(2, 3))
print(sumar(2, 3, op = "-"))

# Para funciones con varios argumentos
def suma_total(*numeros):
    return sum(numeros)

print(suma_total(1, 2, 3, 4))

# Mezclando argumentos normales y *
def describir_persona(nombre, *caracteristicas):
    print(f"Nombre: {nombre}")
    for n in caracteristicas:
        print(f"-{n}")

describir_persona("Pepe", "Espabilado", "Puntual", "Alegre")

# Función para multiplicar valores
valores = [2, 3, 4]

def multiplicar_valores(*valores):
    total = 1
    for n in valores:
        total *= n
    return total

print(multiplicar_valores(*valores))
print(*valores) #Imprime lo que hay dentro del array

