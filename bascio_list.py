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
append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
    Create Read Update - Delete
criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40] # Criar
#numero = lista[2] # pegando um valor da lista
#print(numero)
lista[2] = 300 # Alterar
del lista[3] # Apagar
print(lista)
print(lista[2]) 


lista.append(50) # Adicionar
lista.pop() # Remove o ultimo item da lista
lista.append(60)
lista.append(70)

print(lista)

ultimo_valor = lista.pop()
ultimo_valor = lista.pop(2) # excluir um item expecifico 
print(lista, 'Removido,', ultimo_valor)

# Alguns exemplos

lista = [10, 20, 30, 40]
lista.append('Luciano')
nome = lista.pop()
#print(lista, nome)
#print(lista, lista.pop())
lista.append(1233)
del lista[-1]
#lista.clear()
lista.insert(0, 5) # local da lista e depois o valor
print(lista)
