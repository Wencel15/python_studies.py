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
