import os 

# Criação de um dicionário com os tipos de operações
menu = {
    "0": "Mostrar portfólio",
    "1" : "Alugar um carro",
    "2" : "Devolver um carro"
}

cars = {
    "Chevrolet Tracker" : "R$ 120 /dia",
    "Chevrolet Onix" : "R$ 90 /dia",
    "Hyndai HB20" : "R$ 85 /dia",
    "Hyundai Tucson" : "R$ 120 /dia",
    "Fiat Uno" : "R$ 60 /dia",
    "Fiat Mobi" : "R$ 70 /dia",
    "Fiat Pulse" : "R$ 130 /dia",
}

"""
    operations = {
    "Chevrolet Tracker" : 120,
    "Chevrolet Onix" : 90,
    "Hyndai HB20" : 85,
    "Hyundai Tucson" : 120,
    "Fiat Uno" : 60,
    "Fiat Mobi" : 70,
    "Fiat Pulse" : 130,
}
"""

funcionando = True 

while funcionando:
    i = 0;
    
    print("Bem vindo ao Software de Locadora de Carros")
    print("")
    print("O que deseja fazer?")
    for op, name in menu.items():
        print(i, ":", name)
        i += 1
    print("")
    escolha = input()
    escolha_string = list(menu.keys())[int(escolha)]
    
    print("")
    print(">>> {} escolhida.".format(escolha_string))
    print("")
    
    if (escolha=='0'):
        # Exibindo as informações do dicionário na tela
        i=0
        for op, name in cars.items():
            print(i, ":", name)
            i += 1
            
        print("")
        print("0 - CONTINUAR | 1 - SAIR")
        saida = input()
        
        if(saida=='0'):
            print('')    
            continue 
        elif(saida=='1'):
            break
        else:
            print("Valor informado é inválido. Sistema Encerrado.\n")
    if(escolha=='1'):
        print("[ALUGAR] Dê uma olhada em nosso portifólio de carros:")
        # Exibindo as informações do dicionário na tela
        i=0
        for op, name in cars.items():
            print("[", i, "]", op, "-", name)
            i += 1
            
        print("")
        print("Escolha o codigo do carro")
        codigo_carro = input()
        qtd_dias=input("Informe a quantidade de dias")
        valor_total = preco * qtd_dias
        print(f"Você escolher NOME DO CARRO {codigo_carro} por {qtd_dias}.")
        print(f"O aluguel totaliza R${valor_total}. Deseja alugar?")
        alugar=input()
        if alugar=='0':
            print("Você escolheu alugar")
        elif alugar =='1':
            print("Você escolheu não alugar")
    if(escolha=='2'):
        pass