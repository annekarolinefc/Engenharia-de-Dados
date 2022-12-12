import numpy as np
arrayA = np.arange(2, 21, 2)
arrayA

# ADICIONA 3 para cada elemento criando um novo array numpy
arrayB = 3 + arrayA
# sUBTRAI 4 para cada elemento criando um novo array numpy
arrayC = arrayA - 4
# MULTIPLICA cada elemento por 5 criando um novo array numpy
arrayD = arrayA * 5
# DIVIDE cada elemento por 2 criando um novo array numpy
arrayE = arrayA /2 

print(f'arrayA = {arrayA}\n')
print(f'arrayB = 3 + arrayA = {arrayB}')
print(f'arrayC = arrayA - 4 = {arrayC}')
print(f'arrayD = arrayA * 5 = {arrayD}')
print(f'arrayE = arrayA / 2 = {arrayE}')