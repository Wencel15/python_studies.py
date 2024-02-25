"""
Introdução ao desempacotamento + tuples (tuplas)
"""

#nomes = ['Maria', 'Helena', 'Luiz']
#nome1, nome2, nome3 = nomes
#print(nome2)

#2
#nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
#print(nome3)

#variavel de resto '_'

nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1, _)
