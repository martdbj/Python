def comprobar_validez_prestamos(importe):
    if importe < 1000:
        print("Error: El importe mínimo debe de ser de 1,000.00€")
        return False
    elif importe > 50000:
        print("Error: El importe máximo de solicitud es 50,000.00€")
        return False

    return True

try:
    while True:
        importePrestamo = int(input("Ingrese el importe del préstamo deseado (entre 1,000€ y 50,000€): "))
        if not comprobar_validez_prestamos(importePrestamo):
            print("----------------------------------------------")
            continue
        print(f"Éxito: Solicitud de {importePrestamo}€ procesada.")
        break

except ValueError:
    print(f"Error de formato: Asegúrese de ingresar un valor numérico válido")
else:
    print("----------------------------------------------")
finally:
    print("Sistema de validación de prestamos terminado")

