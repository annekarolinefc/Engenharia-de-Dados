
print("LIST COMPREHENSION")
print("Metodo que escreve uma lista com apenas uma linha")
word = "string"
print(f"Palavra que deseja-se iterar: {word}")

print(f"Iteração utilizando for...")
list_words = []
for w in word:
    list_words.append(w)
    
print(f'Resultado: {list_words}')

print(f"Iteração utilizando list comprehension...")
# Regras: puxa o for e repete o w no inicio 
lc_list_words = [(w) for w in word]
print(f'Resultado: {lc_list_words}')
