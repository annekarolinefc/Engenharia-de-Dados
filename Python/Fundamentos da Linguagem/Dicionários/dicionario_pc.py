meu_pc = {
    "registro": "0001",
    "produto": "notebook", 
    "modelo": "Macbook", 
    "conexões": ["usb-c", "usb", "p2", "hdmi"],
    }

# Adicionando itens periféricos - mouse e teclado
meu_pc["perifericos"]= ["mouse", "teclado"]

print(meu_pc)

print(f"CHAVES DO DICIONARIOS: \n {meu_pc.keys()} \n")
print(f"VALORES DO DICIONARIOS: \n {meu_pc.values()} \n")
print(f"CHAVE/VALOR DO DICIONARIOS: \n {meu_pc.items()} \n")