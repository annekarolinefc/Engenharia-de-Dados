# Semelhante a uma lista, porem numero nao se repetem
x = set()
print(x)

# Adicionando
x.add(1)
print(x)

x.add(2)
print(x)

x.add(3)
print(x, '\n')

# nao adiciona valores repetidos
print("Inserindo valores repetidos:")
x.add(3)
print(x)

x.add(3)
print(x, '\n')

print('Recebendo uma lista e removendo os valores repetidos:')
l = [1, 2, 3, 4, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 9, 9, 10]
print(f'Lista: {l}')
print(f'Tamanho da Lista: {len(l)}\n')
l1=set(l)
print(f'Removendo duplicadas: {l1}')
print(f'Unindo listas: {x.union(l1)}')

print(f'Obtendo valores que são a interceção dos dois: {x.intersection(l1)}')