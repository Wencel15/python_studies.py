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

while contador <= 100:
    contador += 1

    if contador == 6: # não mostra o numero 6 mas continua contado
        continue

    if contador >= 10 and contador <= 27: # não mostra o intervalo de numeros mas continua contando.
        continue

    if contador == 40:
        break

print('Acabou')

"""
While + While
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1

    linha += 1

print('Acabou')
