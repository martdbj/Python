lista = ["1234", "admin", "password", "segura", "admin123", "secreta", "admin123", "admin"]
print("Lista de contraseñas actuales:", lista)
password = input("Introduce tu contraseña: ")
if password in lista:
    print("Esa pw ya la has usado:", lista.count(password), "veces")
    # Pide una nueva contraseña y cambiala por esta repetida
    password = input("Introduce una nueva contraseña: ")
    n = 0



else:
    print("Muy bien, nueva password")