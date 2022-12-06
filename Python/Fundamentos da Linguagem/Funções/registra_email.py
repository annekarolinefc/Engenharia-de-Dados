# função chamada “registro_email” que realize o registro de um email, a partir do nome do usuário e do domínio que o usuário escolher (por exemplo: joao@gmail.com)

def registro_email(nome, dominio):
    return nome+dominio

registro = registro_email('anne', '@gmail.com')
print(f'Registro do e-mail: {registro}')