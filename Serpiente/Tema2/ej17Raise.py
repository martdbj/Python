# Lanzar excepciones 
def validarEdad(edad):
    # Primero validamos que sea un número entero
    if not isinstance(edad, int):
        raise TypeError("La edad deber de ser un número entero")
    if not 0 < edad < 120:
        raise ValueError("La edad debe de estar entre 1 y 119")
    return edad

try:
    miEdad = validarEdad(30)
    miEdad = validarEdad("dsaf")
    miEdad = validarEdad(-5)
    print(f"Tu edad es {miEdad}")
except (TypeError, ValueError) as e:
    print(f"Error al obtener la edad: {e}")