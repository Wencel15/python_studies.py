"""
enumerate - enumera iteráveis (indices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

#lista_enumerada = enumerate(lista)

#for item in lista_enumerada:
#    print(item)


# Outra forma de visualizar 

#for indice, nome in enumerate(lista): # maneira mais simples 
#     print(indice, nome)

#Usando 'list'

#lista_enumerada = list(enumerate(lista))
#lista_enumerada = list(enumerate(lista, start=19))
#print(lista_enumerada)

#for interno

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
