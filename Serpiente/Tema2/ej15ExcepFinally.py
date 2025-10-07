# Ejemplo de finally
archivo = None # Inicializar una variable sin valor inicial

try: 
    archivo = open("mi_archivo.txt", "r")
    contenido = archivo.read()
    print("Contenido del archivo:", contenido)
except FileNotFoundError:
    print("No se encontró el archivo")
finally:
    if archivo: # Nos aseguramos que esté abierto antes de cerrarlo
        archivo.close();
        print("El archivo se ha cerrado")