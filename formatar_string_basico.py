# f - strings

nome = 'Luciano Wencel'
altura = 1.78
peso = 98
imc = peso / (altura * altura)

# Adicionando f''
linha_1 = f'{nome} tem {altura:.2f} de altura' #.2f formatar a quantidade de casas decimais
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2}'


print(linha_1)
print(linha_2)
print(linha_3)


# .format()

a = 'A'
b = 'B'
c = 1.1

string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)
print(formato)

string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
    )

print(formato)

"""
Formatação básica de strings
s = string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o npumero a aparecer antes dos zeros
Sinal - ou +
Ex.: 0>100,.1f
Conversion flags - !r !s !a __repr__ - __str__ - __ask__
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #Colocar caractere a esquerda
print(f'{variavel: <10}') #Colocar caractere a direita
print(f'{variavel: ^10}') #Colocar caractere aos lados
print(f'{1000.4873648123746:.1f}')
print(f'{1000.4873648123746:0=+10,.1f}')
print('O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')
