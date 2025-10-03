# Programa que permite adivinar un número
try:
    userNumber = int(input("Introduce un número: "))
    
    while True:
        guessNumber = int(input("Adivine el número: "))
        if guessNumber == userNumber:
            print("Enhorabuena, lo has adivinado")
            break;
        elif guessNumber < userNumber:
            print("El número que intentas adivinar es mayor")
        else:
            print("El número que intentas adivinar es menor")

except ValueError:
    print("El valor introducido debe de ser un número")