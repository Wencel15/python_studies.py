'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
'''

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    if nome == 'sair':
        break
print('Acabou')

"""
"""

while False: # Quando a condição for falso não entra no while.
    print("EITA")

print('Acabou')

"""
"""
contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)

print('Acabou')

"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

contador = 0 

while contador < 10:
    contador += 1
    print(contador)
