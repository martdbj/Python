import numpy as np
import matplotlib.pyplot as plt

poblacion = np.genfromtxt(
    './poblacion_1_enero.csv',
    delimiter=';',
    dtype=None,
    names=True,
    encoding='utf-8',
    max_rows=21
)

animales = np.genfromtxt(
    './censo_animales.csv',
    delimiter=';',
    dtype=None,
    names=True,
    encoding='utf-8'
)
poblacion['distrito'] = np.char.strip(poblacion['distrito'])
poblacion['distrito'] = np.char.upper(poblacion['distrito'])
distrito_personas = poblacion['distrito']
num_personas = poblacion['num_personas']

animales2024 = animales[animales['\ufeffAÑO'] > 2023]
distrito_perros = animales2024['DISTRITO']
num_perros = animales2024['ESPECIE_CANINA']

max_personas = num_personas.max()
min_personas = num_personas.min()
max_perros = num_perros.max()
min_perros = num_perros.min()

num_personas_normalizado = (num_personas - min_personas) / (max_personas - min_personas)
num_perros_normalizado = (num_perros - min_perros) / (max_perros - min_perros)

size = num_personas / 1.5
plt.scatter(num_personas_normalizado, num_perros_normalizado, s=size)
plt.xlabel('Número de personas (normalizado)')
plt.ylabel('Número de perros (normalizado)')
plt.title('Relación entre personas y perros (normalizado)')
plt.show()
