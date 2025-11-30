from datetime import datetime

ahora = datetime.now()
print("Hora actual: ", ahora)

# Formatear la fecha en distintos estilos
print("Formato corto: ", ahora.strftime("%d/%m/%Y"))
print("Formato largo: ", ahora.strftime("%A, %d de %B de %Y"))

nacimiento = datetime(2005, 10, 21)
hoy = datetime.today()
edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
print("Edad: ", edad)

# Sumar o restar días a una fecha
from datetime import timedelta
fecha_futura = ahora + timedelta(days = 30)
print("Me tienes que pagar el : ", fecha_futura)

# Mostar información de objeto time
from datetime import time
hora_clase = time (8, 30, 0)
print("Hora de clase: ", hora_clase)
print("Hora: ", hora_clase.hour)
print("Minutos: ", hora_clase.minute)

# Calcular el tiempo de ejecución de un bloque de código
import time
inicio = time.time()
for i in range(1000000):
    pass
fin = time.time()

tiempo_ejecucion = fin - inicio
print("Tiempo de ejecución: ", tiempo_ejecucion, " segundos")

import calendar
print(calendar.month(2025, 10))
# Calcular si 2025 es bisiesto
print("Es bisisesto: ", calendar.isleap(2025))
# Cuantos bisiestos hay entre dos días
print("Entre 2000 y 2025: ", calendar.leapdays(2000, 2025))