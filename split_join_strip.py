"""
split e join com list e str
split - divide uma string
join - une uma string
"""
frase = 'Olha só que, coisa interessante'
lista_frases = frase.split(', ')# Quebra no caractere informado, -colocar espaço-
lista_palavras = frase.split()# Quebra nos espaços
print(lista_frases)
print(lista_palavras)

# utilizando o FOR

frase = 'Olha só que, coisa interessante'
lista_frases = frase.split(', ')

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip()) #strip corta os espaços do começo e do fim
    print(lista_frases[i].rstrip()) #rstrip corta os espaços da direita
    print(lista_frases[i].lstrip()) #lstrip corta os espaços da esquerda



# Alterar o indice da lista

for i, frase in enumerate(lista_frases):
    lista_frases[i] = lista_frases[i].strip()
print(lista_frases)



#Adicionar

lista_frases_cruas = frase.split(', ')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())
print(lista_frases)    
print(lista_frases_cruas)

#Join

frases_unidas = '-'.join(lista_frases)
print(frases_unidas)
