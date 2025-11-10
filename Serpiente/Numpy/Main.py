import numpy as np
import matplotlib.pyplot as plt

#https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html
animales = np.genfromtxt(
    './censo_animales.csv',
    delimiter=';',
    dtype=None,
    names=True,
    encoding='utf-8'
)

animales2024 = animales[animales['\ufeffAÑO'] > 2023]
distrito = animales2024['DISTRITO']
numero_perros = animales2024['ESPECIE_CANINA']

#https://python-charts.com/es/ranking/grafico-barras-matplotlib/
fig, ax = plt.subplots()
plt.xticks(rotation=45, ha='right')
ax.bar(x=distrito, height=numero_perros)
plt.show()

print(distrito)
print(numero_perros)


