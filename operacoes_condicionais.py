# if / elif / else
#se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')

#Exemplo 2

condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = True


if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

print('Fora do if')

# exemplo 3 

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior do que {segundo_valor}')
else:
    print(f'{segundo_valor} é maior do que {primeiro_valor}')
