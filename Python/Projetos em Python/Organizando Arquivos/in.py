# Organizar pastas por tipo
# %%
# Importa o módulo 0S
import os

# %%
# cria variável com o caminho atual
cwd = os.getcwd()

# %%
# Lista TODOS os arquivos e diretorio do caminho atual
full_list = os.listdir(cwd)
full_list

# mesmo resultado: [i for i in full_list]
# %%
# removendo os arquivos .py da lista - Lista todos os arquivos exceto os com extensao .py
files_list = [i.lower() for i in full_list if os.path.isfile(i) and '.py' not in i]

files_list

# %%
# exibindo o tipo de arquivo do diretorio- lista
types = list(set([i.split('.')[-1] for i in files_list]))
for file_type in types:
    os.mkdir(file_type)
# %%
types

# %%
# Cria a pasta com as extensoes 
for file_type in types:
    os.mkdir(file_type)

# %%
# ENVIANDO OS ARQUIVOS PARA CADA PASTA
for file in files_list:
    from_path = os.path.join(cwd, file)
    to_path = os.path.join(cwd, file.split('.')[-1])
    to_path = os.path.join(to_path, file)
    os.replace(from_path, to_path)
    
## OU O COMANDO ABAIXO
# %%
for file in files_list:
    path_from = cwd + '/' + file
    path_to = cwd + '/' + file.split('.')[-1] + '/' + file
    os.replace(path_from, path_to)