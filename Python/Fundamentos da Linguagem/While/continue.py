print("EXEMPLO DE CONTINUE")
print("Quando o codigo encontra o continue, ele para de executar tudo que esta abaixo.")
x = 0
while x<10:
    print(f'O valor de x é: {x}')
    x+=1
    continue 
    print('X ainda é menor que 10. Incrementando...') #ignorou esse trecho
else:
    print('Concluído')