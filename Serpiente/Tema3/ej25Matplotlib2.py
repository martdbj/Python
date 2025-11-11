import  matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01) #Coordenada X
s = 1 + np.sin(2 * np.pi * t)
plt.plot(t, s)
#Completar la gráfica
#Etiqueta en el eje X
plt.xlabel('tiempo(s)')
plt.ylabel('voltaje (mV)')
#Título
plt.title("Gráfico simple de DAW")
plt.grid(True)
plt.savefig('ej25Imagen.png')
plt.show()
