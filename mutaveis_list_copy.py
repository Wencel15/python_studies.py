"""
Cuidado com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

#nome = 'Luciano'
#noutra_variavel = nome
#nome = 'Luiz'
#print(nome)
#print(noutra_variavel)

lista_a = ['Luciano', 'Luiz']
lista_b = lista_a # duas listas apontar para o mesmo valor na memoria
print(lista_b)

lista_a[0] = 'Qualquer coisa'
print(lista_b) # mesmo alterando a lista a, da mesma maneira ainda busca o valor alterado na memora e retorna b = a 

# 2 

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
