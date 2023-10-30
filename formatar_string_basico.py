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
