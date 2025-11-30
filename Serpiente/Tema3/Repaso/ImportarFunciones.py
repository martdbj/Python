# 1. Importar modulo funciones sin usar alias
import ModulosFunciones

# Usamos el factorial
print(ModulosFunciones.factorial(5))
print(ModulosFunciones.PI)


# 2. Importación módulo con alias
import ModulosFunciones as mf
print(mf.calcular_area_circulo(4.5))


# 3. Importación selectiva de función (Se utiliza from)
from ModulosFunciones import factorial
print(factorial(6))


# 4. Importación selectiva de multiples elementos
from ModulosFunciones import calcular_area_circulo, PI
print(calcular_area_circulo(10))
print(PI)


# 5. Importación selectiva de alias
from ModulosFunciones import fibonacci as serie_fibo
print(serie_fibo(10))
    
