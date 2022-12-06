def gera_numeros_impares(valorLimite):
    return [i for i in range(valorLimite) if (i%2!=0)] #if (i%2==1)

lista = gera_numeros_impares(21)
print(f"Lista de numeros impares: {lista}")
print('\n')
print(f"Tipo: {type(gera_numeros_impares)}") # retorna function 
print(f"Tipo: {type(gera_numeros_impares(21))}") # retorna lista (retorno de dentro da função)