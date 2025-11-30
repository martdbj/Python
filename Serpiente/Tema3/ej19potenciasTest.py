# Para importar otra clase usamos import
import ej19potencias

# Con dir() vemos los elemenots definidos en un módulo
print(dir(ej19potencias))
print(ej19potencias.cuadrado(3))

# Se pueden usar alias
import ej19potencias as p
print(p.cubo(3))

# Pdemos importar varios elementos separados por comas
from ej19potencias import cubo, cuadrado
# Poner alias
from ej19potencias import cubo as pcubo, cuadrado as pcuad
print(pcubo(3))
print(pcuad(5))