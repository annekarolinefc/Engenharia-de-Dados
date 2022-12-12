# 3 inputs numericos: start, stop e step.
import numpy as np
array3 = np.arange(5)
array4 = np.arange(0, 11, 2)
array5 = np.zeros(5)
array6 = np.ones(4)
array7 = np.ones((4, 6))
array8 = np.linspace(1, 2, 9)
array_random = np.random.randint(1, 50, 20) # 20 valores entre 1 e 50

print(f'Array Numpy:\n {array3}\n')
print(f'Array Numpy:\n {array4}\n')
print(f'Array Numpy:\n {array5}\n')
print(f'Array Numpy:\n {array6}\n')
print(f'Array Numpy:\n {array7}\n')
print(f'Array Numpy:\n {array8}\n')
print(f'Array Numpy:\n {array_random}\n')