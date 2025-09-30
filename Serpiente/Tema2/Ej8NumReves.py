# Pide un número de 5 cifras
# Usando operaciones sencillas pinta el número al revés

numero = 12345
numerofinal = ""

for i in range(5):
    numerofinal += str((numero % 10)) 
    numero //= 10

print(numerofinal)