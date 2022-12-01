import os 
print("==========")

# Criação de um dicionário com os tipos de operações
operations = {
    "+" : "Soma",
    "-" : "Subtração",
    "*" : "Multiplicação",
    "/" : "Divisão",
    "**" : "Exponenciação",
}

while True:
    #Limpa o terminal
    os.system("clear")
    i = 0
    
    #Acessando o dicionario e imprimindo no terminal
    for op, name in operations.items():
        print(i, ":", name)
        i += 1
    print("")
    print("Escolha a operação que deseja realizar:")
    op = input()
    #list(operations.keys()) => ['+','-', '*', '/', '^'] - ao escolher [int(op)], acessa o numero no dicionario
    op_string = list(operations.keys())[int(op)]

    print("")
    print(">>> {} escolhida.".format(op_string))
    print("")
    print("Qual o primeiro valor?")
    v1 = float(input())
    print("Qual o segundo valor?")
    v2 = float(input())

    if op == '0':
        result = v1 + v2
    elif op == '1':
        result = v1 - v2
    elif op == '2':
        result = v1 * v2
    elif op == '3':
        result = v1 / v2
    elif op == '4':
        result = v1 ** v2

    print("")
    print("{} {} {} = {}".format(v1, op_string, v2, result))
    print("")
    print("===========")
    print("Deseja fazer outra operação? 0 - SIM, 1 - NÃO")
    if float(input()) == 1:
        break
        