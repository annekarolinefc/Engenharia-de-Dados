import numpy as np

array_random = np.random.randint(1, 50, 20) # 20 valores entre 1 e 50
print(array_random) 

print(f'Maior valor: {array_random.max()}')
print(f'Menor valor: {array_random.min()}')

print(f'Indice do maior valor: {array_random.argmax()}')
print(f'Indice do menor valor: {array_random.argmin()}')