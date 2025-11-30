def operar(a, b):
    global suma
    suma = a + b
    resta = a - b
    print(suma, resta)

operar(4, 5)
print(suma) # Puedo imprimir la variable suma debido a que es una variable decalrada como global
# print(resta) No funciona al no ser global

PI = 3.1415
def area(radio):
    return PI * radio ** 2

print(area(2))

