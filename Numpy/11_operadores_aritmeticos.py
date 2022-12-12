import numpy as np

arrayA = np.arange(1, 21, 2)
print(f'ArrayA: {arrayA}')

arrayB = np.arange(1, 11)
print(f'ArrayB: {arrayB}\n')

print(f'ArrayA + ArrayB: {arrayA+arrayB}')
print(f'ArrayA - ArrayB: {arrayA-arrayB}')
print(f'ArrayA * ArrayB: {arrayA*arrayB}')
print(f'ArrayA / ArrayB: {arrayA/arrayB}\n')


arrayC = np.array([[1, 2, 3], [4, 5, 6]])
print(f'ArrayC: {arrayC}')
arrayD = np.array([[7, 8, 9], [10, 11, 12]])
print(f'ArrayD: {arrayD}\n')

print(f'ArrayC + ArrayD: {arrayC+arrayD}')
print(f'ArrayC - ArrayD: {arrayC-arrayD}')
print(f'ArrayC * ArrayD: {arrayC*arrayD}')