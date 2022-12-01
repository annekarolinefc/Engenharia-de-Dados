soma = lambda x,y:(x+y)
subtracao = lambda x,y:(x-y)
divisao = lambda x,y:(x/y)
multiplicacao = lambda x,y:(x*y)
exponenciacao = lambda x,y:(x**y)

funcionando = True 
while funcionando:
    opcao = int(input("""
        0 : Soma
        1 : Subtração
        2 : Multiplicação
        3 : Divisão
        4 : Exponenciação
        5 : Encerrar Calculadora
        
        Escolha a operação que deseja realizar:
        """))

    if (opcao == 0):
        print("Você escolheu SOMA...\n")
        numero_1 = float(input("Informe o primeiro numero:"))
        numero_2 = float(input("Informe o segundo numero:"))
        print(f'{numero_1}+{numero_2}')
        print(f'A soma de {numero_1} e {numero_2} é igual a {soma(numero_1, numero_2)}\n')
    elif(opcao ==1):
        print("Você escolheu SUBTRAÇÃO...\n")
        numero_1 = float(input("Informe o primeiro numero:"))
        numero_2 = float(input("Informe o segundo numero:"))
        print(f'{numero_1} - {numero_2}')
        print(f'A subtração de {numero_1} e {numero_2} é igual a {subtracao(numero_1, numero_2)}\n')
    elif(opcao ==2):
        print("Você escolheu MULTIPLICAÇÃO...\n")
        numero_1 = float(input("Informe o primeiro numero:"))
        numero_2 = float(input("Informe o segundo numero:"))
        print(f'{numero_1} * {numero_2}')
        print(f'A multiplicação de {numero_1} e {numero_2} é igual a {multiplicacao(numero_1, numero_2)}\n')
    elif(opcao ==3):
        print("Você escolheu DIVISÃO...\n")
        numero_1 = float(input("Informe o primeiro numero:"))
        numero_2 = float(input("Informe o segundo numero:"))
        print(f'{numero_1} / {numero_2}')
        print(f'A divisão de {numero_1} por {numero_2} é igual a {divisao(numero_1, numero_2)}\n')
    elif(opcao ==4):
        print("Você escolheu EXPONENCIAÇÃO...\n")
        numero_1 = float(input("Informe o primeiro numero:"))
        numero_2 = float(input("Informe o segundo numero:"))
        print(f'{numero_1} ** {numero_2}')
        print(f'A exponenciação de {numero_1} por {numero_2} é igual a {exponenciacao(numero_1, numero_2)}\n')
    elif(opcao ==5):
        funcionando = False
        print("A calculadora foi encerrada\n")
        break
    else:
        print("Você digitou uma opção inválida.\nCalculadora encerrada.")
        
# Uso de operações aritmeticas, função lambda, formatação, condição, laço de repetição