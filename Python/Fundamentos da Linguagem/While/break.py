print("EXEMPLO DE BREAK")
print("Interrompe o laço. Para de executar.")
x = 0
while x<10:
    print(f'O valor de x é: {x}')
    x+=1
    break
    print('X ainda é menor que 10. Incrementando...') #ignorou esse trecho
else:
    print('Concluído')
print('Quebra de laço')