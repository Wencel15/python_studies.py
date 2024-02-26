"""
Desempacotamento em chamadas
de métodos e funções
"""
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

#a, b, c = lista
#print(a, c)


for nome in lista:
    print(nome)
    #print(nome, end=' ')#desempacotar em linha

print(*lista)#como se fosse usar o FOR
print(*string)
print(*tupla)


#chamar o ultimo elemento

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

p, b, *_, u = lista
#print(a, u)
