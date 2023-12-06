frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido Van Rossum.'

#print(frase.count('Python')) # Manueira simples de contar quantas veses strings aparecem dentro do testo com .count


i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase): # iterando a string
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
 
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_que_apareceu_mais_vezes = letra_atual

    
    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_que_apareceu_mais_vezes}" que apareceu ' 
    f'{qtd_apareceu_mais_vezes} x'
)
