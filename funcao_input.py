nome = input('Qual o seu nome? ') #Sempre vai retornar uma str
print(f'O seu nome é {nome}')
print(f'O seu nome é {nome=}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro npumero: ')

print(f'A soma dos números é: {numero_1 + numero_2}') #vai concatenar e não somar


int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
print(f'A soma dos números é: {int_numero_1 + int_numero_2}') 
