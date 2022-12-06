print(f"Resto da divisao de 5 por 2 => 5%2 => {5%2} => Resto 1 sempre que for impar")

lista_pares = []
lista_impares = []

for i in range(100):
    # se for divisivel por 2

    if (i%2==0):
        print(f"É par: {i}")
        lista_pares.append(i)
    else:
        print(f"É impar: {i}")
        lista_impares.append(i)
print('/n')
print(f'Lista de valores impares: {lista_impares}')
print(f'Lista de valores pares: {lista_pares}')