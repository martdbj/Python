x = 3
print("*************INT")
print(x, "El tipo es: ", type(x))
print(x + 1); print(x - 1), print(x ** 2) # La potencia es **

# Más ejemplos
x += 1
print(x)
x *= 2
print(x)

print("*************FLOAT")
y = 2.5
print(y, "El tipo es: ", type(y))
print(y, y + 1, y * 2, y ** 2)

print("*************BOOLEAN")
t,f = True, False
print(t, f); print(type(t), type(f))
print(t and f)
print(t or f)
print(not t)
print(t != f)

print("*************CADENAS")
hello = 'hello'
world = "world"
print(hello, world, len(hello))
# Concatenación
hw = hello + ' ' + world
print(hw)
# Funciones sobre cadenas
s = "hello"
print(s.upper())
print(s.capitalize())
print(s.rjust(7)) # Justifica a la derecha con 7 espacios
print(s.replace('l', '(ell'))