import numpy as np

animales = np.genfromtxt(
    './censo_animales.csv',
    delimiter=';',
    dtype=None,
    names=True,
    encoding='utf-8'
)

animales2024 = animales[animales['\ufeffAÑO'] > 2023]
print(animales2024)



