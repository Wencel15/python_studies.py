"""
Listas em Puthon
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Metodos uteis: append, insert, pop, clear, extend, +
"""

string = 'ABCDE' # 5 Caracteres (len)
#lista = []
#print(lista, type(lista))
#print(bool([])) # falsy

#1
lista = [123, True, 'Luciano Wencel', 1.2, []]
print(lista)
print(lista[2].upper(), type(lista[2]))

#2
lista[-3] = 'Maria'
print(lista[2].upper(), type(lista[2]))

#3
print(lista)

"""
Create Read Update - Delete
criar, ler, alterar, apagar = lista[i] (CURD)
"""

lista = [10, 20, 30, 40] # Criar
#numero = lista[2] # pegando um valor da lista
#print(numero)
lista[2] = 300 # Alterar
del lista[3] # Apagar
print(lista)
print(lista[2]) 