# Funcion que procesa el pago de imjpuestos (que sea número, que sea positivo > 0)
class ErrorCantidadInvalida(Exception):
    def __init__(self, cantidad, mensaje = "La cantidad debe ser positiva"):
        self.cantidad = cantidad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def procesar_pago(cantidad):
    if isinstance(cantidad, int):
        raise TypeError("La cantidad debe de ser un número entero")
    
    if cantidad <= 0:
        raise ErrorCantidadInvalida(cantidad)
    
    print(f"Procesando el pago: {cantidad}")

try:
    procesar_pago(3)

    procesar_pago("sdfsf")

except (ErrorCantidadInvalida, TypeError) as e:
    print(f"Error en la ejecución: {e}")