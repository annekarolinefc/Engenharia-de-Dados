# Deve ficar no mesmo nível do arquivo que estou trabalhando

# %% 
import os

# %%
#Retorna uma string contendo o caminho completo até onde estou (diretório atual)
os.getcwd()

# %%
# Retorna uma lista contendo todos os arquivos e pastas no diretório onde estou
os.listdir()

# %%
# Me lista o que tem nesse diretório
os.listdir('c:\\Users\\Anne Karoline\\OneDrive\\Área de Trabalho\\github\\Engenharia-de-Dados\\Python\\Fundamentos da Linguagem\\Modulo OS')

# %%
# Vai trocar o diretório padrão onde meu código está sendo executado
diretorio_atual = os.getcwd()
print(f'Diretorio atual: {diretorio_atual} \n')
novo_diretorio = 'c:\\Users\\Anne Karoline\\OneDrive\\Área de Trabalho\\github\\Engenharia-de-Dados\\Python\\Fundamentos da Linguagem'
print(f'Novo Diretorio: {novo_diretorio} \n')

os.chdir(novo_diretorio)
print(f'Exibindo novo diretorio: {os.getcwd()}')

# %%
# Criando uma pasta 

# ver diretorio
os.getcwd()
# muda diretorio
os.chdir(diretorio_atual)
#cria pasta
os.mkdir('Pasta criada com mkdir')

# %%
# Renomear arquivo
os.chdir('c:\\Users\\Anne Karoline\\OneDrive\\Área de Trabalho\\github\\Engenharia-de-Dados\\Python\\Fundamentos da Linguagem\\Modulo OS\\Arquivos para teste')

# diz qual o nome atual e qual o nome que deseja que o arquivo tenha
os.rename('teste.txt', "teste2.txt")

# %%
# Renomear diretório
os.chdir('c:\\Users\\Anne Karoline\\OneDrive\\Área de Trabalho\\github\\Engenharia-de-Dados\\Python\\Fundamentos da Linguagem\\Modulo OS\\Arquivos para teste')

# diz qual o nome atual e qual o nome que deseja que o diretorio tenha
os.rename('Pasta', "Pasta2")

# %%
# Movimentar arquivo
os.chdir('c:\\Users\\Anne Karoline\\OneDrive\\Área de Trabalho\\github\\Engenharia-de-Dados\\Python\\Fundamentos da Linguagem\\Modulo OS\\Arquivos para teste')

os.rename('Pasta2', 'Pasta3/Pasta2')

#retrocedendo...
os.rename('Pasta3/Pasta2', 'Pasta2')

# %%
# remove arquivo APENAS
os.remove('teste.csv')

# %%
# remove diretório
os.rmdir('Pasta2')

# %%
#Sistema retorna data e horario
cmd='date'
os.system(cmd)

# %%
