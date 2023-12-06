"""
while/else
"""

string = 'Valor qualquer'

i = 0 

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break ### Toda vez que um break é executado ele sai fora do while e não executa o else.

    print(letra)
    i += 1

else:
    print('O else foi executado.')

print('Fora do while.')
