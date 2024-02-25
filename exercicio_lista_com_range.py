"""
Exercicio
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']

lista.append('João')

indices = range(len(lista))

for indices in indices:
    print(indices, lista[indices], type(lista[indices]))
