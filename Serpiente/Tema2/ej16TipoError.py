# Para obtener información de un error
cad = "hola"
try: 
    i = int(cad)
except ValueError as error:
    print(type(error))
    print(error)