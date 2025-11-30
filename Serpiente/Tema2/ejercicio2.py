from datetime import datetime
import shutil 

ahora = datetime.now()
ahora = ahora.strftime("%Y-%m-%d")
source = "D:/origenMD"
destination = f"D:/backup/{ahora}Ejercicios"

try:
    shutil.copytree(source, destination)
    print("Backup Realizado")
except FileExistsError:
    print("Error. Un archivo igual ya existe en la carpeta backup")
except Exception as e:
    print(e)