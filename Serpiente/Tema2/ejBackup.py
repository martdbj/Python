from datetime import datetime
import shutil 

ahora = datetime.now()
ahora = ahora.strftime("%d-%m-%Y")
source = "D:/origenMD"
destination = f"D:/backup/{ahora}Ejercicios"

try:
    shutil.copytree(source, destination)
    print("Backup Realizado")
except Exception as e:
    print(e)