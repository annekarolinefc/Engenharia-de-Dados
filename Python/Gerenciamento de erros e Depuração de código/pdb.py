#pip install pdbpp

# %% 
import pdb

x = [1, 2, 3]
y = 2
z = 3

print(x+y)

#Congela o trecho de código - Executa tudo acima e abre o terminal interativo do python
pdb.set_trace()

print(x+y)

# %%
