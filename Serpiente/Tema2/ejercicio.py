import shutil
from datetime import datetime
# Shutil.copy

source = "D:/origenMD/datosImportantes.txt"
destination = "D:/destinoMD/backUpDatos.txt"

try:
    shutil.copy(source, destination)
    print("Back")
except Exception as e:
    print(e)

# Shutil.copyTree
ahora = datetime.now()
ahora = ahora.strftime("%d-%m-%Y")
source = "D:/origenMD"
destination = f"D:/backup/{ahora}Ejercicios"

try:
    shutil.copytree(source, destination)
    print("Backup Realizado")
except Exception as e:
    print(e)