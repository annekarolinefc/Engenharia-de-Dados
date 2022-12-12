import numpy as np
array0 = np.array([])
## Encontrando a forma
print(f'Forma do Array: {array0.shape}')

array1 = np.array([1, 2, 3, 4, 5])
## Encontrando a forma
print(f'Forma do Array: {array1.shape}')

array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
## Encontrando a forma
print(f'Forma do Array: {array2.shape}')

array3 = np.array([[1, 2, 3, 3], [4, 5, 6, 4], [7, 8, 9, 9]])
## Encontrando a forma
print(f'Forma do Array: {array3.shape}')
print(f'Alterando a Forma do Array: {array3.reshape(12)}')
print(f'Alterando a Forma do Array: {array3.reshape(3, 4)}')