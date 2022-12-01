try:
    x = [1, 2, 3]
    y = 1
    x+y
except Exception as e:
    print(f'Erro na execução: {e}')
finally:
    print('Fim do bloco de código.')