import signal

import numpy as np
# Leemos el archivo iris.csv, lo cargamos en una matriz y descartamos la primera fila y decimos que el separador es una coma
iris = np.loadtxt('./iris.csv', skiprows=1, delimiter=',',) #, para decir que no hay mas parámetros
print("Matriz a partir de archivo de datos \n", iris.shape)

#1- Selecciona 5 filas y calcula la media
print("Media de las 5 primeras filas: ", np.mean(iris[0:5, :]))

#2- Usando axis de mean calcula la media de las columnas
print("Media de las columnas: ", np.mean(iris, axis=0))

#3- Encuentra el valor mínimo de cada característica np.min
print("Valor mínimo de cada característica: ", np.min(iris, axis=0))

#4- Devuelve todas las filas con largo de pétalo (col2) mayor que 5
print("Filas con largo pétalo > 5: \n", iris[iris[:, 2] > 5])

#5- Filas de 50 a 99 pero solo las columnas largo y ancho del pétalo (2 y 3)
print("Filas 50 a 99 con largo y ancho pétalo: \n", iris[50:100, 2:4])

#6- Normalizar para que los valores estén en el rango 0-1 (X - Xmin / Xmax - Xmin)
min_iris = iris.min()
max_iris = iris.max()
print("Array Iris normalizado: \n", (iris - min_iris) / (max_iris - min_iris))

#7- Guarda las 4 primeras columnas en una variable llamada x
x = iris[:, 0:4]
print("X es: \n", x)

#8- Guarda la última columna en una variable Y
y = iris[:, 4]
print("Y es: ", y)
