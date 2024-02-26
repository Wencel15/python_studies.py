"""
Imprecisão de ponto flutuante
Double-precision floating-point formar IEEE 754

"""

numero_1 = 0.1 #os valores salvos na memoria não conseguem ser precisos com pontos flutuantes
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')#retorna uma strig

#função round
print(round(numero_3, 2))# passando o numero de casas decimais


# adicionar um modulo decimal import decimal

import decimal

numero_1 = decimal.Decimal('0.1') 
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
