# Vamos a realizar pruebas con el for
for i in range(1, 6):
    print(i, end = ",")

print("\nOtro ejemplo")
for i in range(7, 10):
    print(i, end = " ")

print("\nOtro ejmplo")
for i in range(10):
    print(i, end = " ")
    if i == 3:
        break
print("\nOtro ejmplo")
nombres = ["Carlos", "Julio", "Esther"]
for i in nombres:
    print(i, " ")