#in -> organiza as pastas por tipo
#out -> retrocede

# %%
import os

# %%
# listar o caminho atual
cwd = os.getcwd()

# %%
# Listar diretórios
folder_list = [i for i in os.listdir(cwd) if os.path.isdir(i)]
folder_list

# %%
for folder in folder_list:
    path = os.path.join(cwd, folder)
    
    files = os.listdir(path)
    for file in files:
        from_path = os.path.join(path, file)
        to_path = os.path.join(cwd, file)
        os.replace(from_path, to_path)
    os.rmdir(path)
# %%

for folder in folder_list:
    path = cwd + '/' + folder
    files = os.listdir(path)
    for file in files:
        path_from = path + '/' + file
        path_to = cwd + '/' + file
        os.replace(path_from, path_to)
    os.rmdir(path)