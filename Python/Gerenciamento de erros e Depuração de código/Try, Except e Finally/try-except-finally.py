# %%
x = [1, 2, 3]
y = 1

x+y
# %%
try:
    x = [1, 2, 3]
    y = 1
    x+y
except:
    print('Erro na execução')
# %%
# Recebendo o erro para trata-lo:
try:
    x = [1, 2, 3]
    y = 1
    x+y
except Exception as e:
    print('Erro na execução:' + e)
# %%
print('ERRO')
# %%
try:
    x = [1, 2, 3]
    y = 1
    x+y
except Exception as e:
    print(f'Erro na execução: {e}')
finally:
    print('Fim do bloco de código.')