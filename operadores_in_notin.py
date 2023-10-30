"""
Operadores in e not in
Strings são interáveis # navegar item a item
 0 1 2 3 4 5 6
 L u c i a n o
-7-6-5-4-3-2-1
"""
nome = 'Luciano'
print(nome[4])
print(nome[-3])

print('a' in nome)
print('z' in nome)

print('r' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que desenha encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está enm {nome}')
else:
    print(f'{encontrar} não está em {nome}')
