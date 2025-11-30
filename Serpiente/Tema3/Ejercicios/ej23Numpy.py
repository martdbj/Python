#Ejercicios con Numpy
import numpy as np

#A
print("Ejerccio A")
a = np.ones((2, 3))
b = np.arange(1, 7).reshape((2, 3))
result_a = a + b
print(result_a)

#B
print("\nEjercicio B")
c = np.arange(1, 6, 2).reshape((3, 1))
d = np.arange(2, 7, 2)
result = c * d
print(result)

#C
print("\nEjercicio C")
c = np.arange(1, 17).reshape((4, 4))
c[c % 2 == 0] = -1
print(c)

#D
print("\nEjercicio D")
d = np.array(np.arange(2, 8).reshape((2, 3)), dtype=complex)
print(d)
