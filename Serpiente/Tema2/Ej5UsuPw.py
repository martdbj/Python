# Programa que pide un nombre de usuario o una contraseña 
# Si se introduce pepe y pepepwd muestra "Has entrado al sistema"
# Si no usaurio incorrecto

nombre = input("Introduzca su nombre de usuario: ")
pwd = input("Introduzca su contraseña: ")
if nombre == "pepe" and pwd == "pepepwd":
    print("Has entrado al sistema")
else:
    print("Error de inicio de sesión")