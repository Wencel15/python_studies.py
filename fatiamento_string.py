"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[-4])
print(variavel[5])
print(variavel[4:]) # Pega do indicado até o final i
print(variavel[4:8]) # Pega o intervalo i:f
print(variavel[:5]) # Do inicio até o intervalo
print(len(variavel[5]))
print(len(variavel))
print(variavel[0:9:2]) # O passo p pula a quantidade de caracteres
print(variavel[::-1]) # Inverte
