"""
Interpolação básica de strings com %
s - string
d e i - int
f - float
x e C - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luciano'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (15, 15)) # numero apos o 0 é o numero de cartacteres exibidos
