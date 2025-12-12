# Métodos de inserción en listas
lista = [1, 2, 3, 4]
print("lista=", lista)
lista2 = [5, 6]
lista.extend(lista2)
print("lista =", lista)
lista.insert(1, 100)
print("lista =", lista)
print("lista.pop() =", lista.pop())
print("lista.pop(1) =", lista.pop(1))
lista.remove(3)
print("lista.remove(3) =", lista)
# Ordenar la lista
lista.reverse()
lista.sort(reverse=True)
print("lista.sort() =", lista)
lista = ["hola", "qué", "tal", "Hola", "Qué", "Tal"]
lista.sort()
print("lista.sort() =", lista)
lista = [1, 2, 3, 4, 5]
print("Cuántos 5 hay?", lista.count(5))
print("En qué posición está el 5?", lista.index(5))
print("Qué número sale", lista.index(5, 1, 6))