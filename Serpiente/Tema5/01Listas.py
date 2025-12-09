lista = [1, 2, 3, 4, 5, 6]
print("Recorriendo la lista")
for num in lista:
    print(num, end=" ")
# Pertenencia
print("Está el 2 en la lista?", 2 in lista)
print("El 8 NO está en la lista?", 8 not in lista)
# Concatenar
lista = lista + [7, 8, 9]
print("Nueva lista", lista)
# Repetición
print("lista * 2", lista * 2)
# Acceder
print("Elemento en posición 4: ", lista[3])
# Slice
print("Subsecuencia de lista: ", lista[2:4])
# Otro slice
print("Subsecuencia de lista con salto: ", lista[1:6:2])
# Número de elementos
print("Longitud: ", len(lista))
# Máximo/Mínimo
print("Máximo: ", max(lista))
print("Mínimo: ", min(lista))
# Como es mutable puedo cambiar un elemento
lista[2] = 99
print("Lista cambiada: ", lista)
lista[2:4] = [80, 90, 100]
print("Lista cambiada 2: ", lista)
# Borrar
del lista[5:]
print("Lista cambiada 3: ", lista)
lista *= 2
print("Lista cambiada 4: ", lista)
