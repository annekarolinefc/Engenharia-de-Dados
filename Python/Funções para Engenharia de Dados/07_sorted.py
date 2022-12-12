# Sentido -> True or False.
# False é default - ascendente

names = ['Aline', 'Spencer', 'Elizabth', 'Diego' , 'Jack', 'Breno']

print(f'Default (False): {sorted(names)}')
print(f'False - ascendente: {sorted(names, reverse=False)}')
print(f'True - descendente: {sorted(names, reverse=True)}\n')

nums = (5, 2, -7, 0 , -4, 1, 18)
print(f'False - ascendente: {sorted(nums, reverse=False)}')
print(f'True - descendente: {sorted(nums, reverse=True)}')