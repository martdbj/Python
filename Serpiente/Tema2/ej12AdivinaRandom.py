# Programa que permite adivinar un número
import random

try:
    random = random.randint(1, 50)

    while True:
        guessNumber = int(input("Adivine el número: "))
        
        if guessNumber < 1 or guessNumber > 50:
            print("El número debe de estar en un rango entre 1 y 50")
            continue
            
        elif guessNumber == random:
            print("Enhorabuena, lo has adivinado")
            break
            
        elif guessNumber < random:
            print("El número que intentas adivinar es mayor")

        else:
            print("El número que intentas adivinar es menor")

except ValueError:
    print("El valor introducido debe de ser un número")