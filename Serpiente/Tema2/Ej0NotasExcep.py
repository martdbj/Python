try:   
    nota = float(input("Introduce una nota de 0 a 10: "))
    
    if 0 <= nota <= 10:
        if nota >= 9:
            print("Sobresaliente")
        elif nota >= 7:
            print("Notable")
        elif nota >= 5:
            print("Aprobado")
        else: 
            print("Suspenso")
    else:
        print("La nota debe etsar entre 0 y 10")
except ValueError:
    print("Error, debes introducir un número válido")