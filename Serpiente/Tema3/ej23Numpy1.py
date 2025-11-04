import numpy as np
print("Version ", np.__version__)

# Un array es una estructura similar a una lista, pero optimizada para cálculos numéricos
a = np.array([1, 2, 3])
print("Mi primer array en numpy: ", a)

print("\n*Crear arrays*")
print("Array de enteros: ", np.array([10, 20,30]))
print("Array de ceros: ", np.zeros(5))
print("Array de unos que tengan 2 filas y 3 columnas")
print(np.ones((2, 3)))
print("Un array desde 0 hasta 10 contando de 2 en 2")
print(np.arange(0, 10, 2))
print("Array con valores aleatorios en 3 filas y 2 columnas")
print(np.random.rand(3, 2))


print("\n*Más ejemplos*")
# Matriz nueva de 2x2
mat1 = np.array([[1, 2], [3, 4]])
print(mat1)

# Matriz de unos de 2x2
mat2 = np.ones((2, 2))
print(mat2)

# Comprobar la dimension de la mat2
print("Dimensión de matriz 2: ", mat2.shape)

# Sumar matrices
matSuma = mat1 + mat2
print("Suma de matrices: \n", matSuma)

# Multiplicar matrices por un valor
matMult = mat1 * 2
print("MatMult: \n", matMult)

# Multiplicación de matrices
print("Mult mat opción 1: \n", np.matmul(mat1, mat2))
print("Mult mat opción 2: \n", mat1 @ mat2)

# Inversa de la matriz
print("Dada la matriz1: \n", mat1)
print("La inversa es: \n", np.linalg.inv(mat1))

# Más ejemplos
# Crear una matriz con valores del 1 al 9 de forma rápida
mat3 = np.arange(1, 10).reshape((3, 3))
print("Matriz del 1 al 9: \n", mat3)
print("Matriz del 1 al 9 transversa: \n", mat3.T) # Transversa de la matriz

# Seleccionar celdas
print("fila2, columna2: ", mat3[1, 1])
print("Toda la fila2: ", mat3[1, :]) # Para seleccionar toda una fila o columna se usa :
print("Columna3: ", mat3[:, 2])
print("Dimensiones mat3", mat3.shape)

#Filtrados
print("De la matriz > 5: \n", mat3[mat3 > 5])
#Media
print("Media de la matriz: ", np.mean(mat3))
print("Media de filas: ", np.mean(mat3, axis = 1))
print("Media de columnas: ", np.mean(mat3, axis = 0))