import numpy as np 
scores = np.random.randint(50, 101, 200)

print(f'Pontuacoes: {scores}\n')
print(f'Mediana: {np.median(scores)}')
print(f'Media: {np.mean(scores)}')
print(f'Variancia: {np.var(scores)}')
print(f'Desvio Padrao: {np.std(scores)}')