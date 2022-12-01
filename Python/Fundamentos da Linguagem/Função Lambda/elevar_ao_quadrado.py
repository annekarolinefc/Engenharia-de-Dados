def elevar_ao_quadrado(x):
    return x ** 2

print(f"Usando função: {elevar_ao_quadrado(4)}")

elevar_ao_quadrado = lambda x:(x**2)
print(f"Usando função lambda: {elevar_ao_quadrado(4)}")
