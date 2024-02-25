"""
Iterável -> str, range, atc ( __iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

#numeros = range(0, 100, 8)

#for numero in numeros:
#    print(numero)

#texto = 'Luiz'.__iter__()
#print(texto)

#Exemplo de iter simplificado
#texto =  iter('Luiz')
#print(texto)

#next
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())

#Exemplo de next simplificado
#print(next(texto))
#print(next(texto))
#print(next(texto))
#print(next(texto))

#2

#for letra in texto
#print(letra)
texto = 'Luiz' # iteravel
iterador = iter(texto) # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

#3

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)

else:
    print('For completo com sucesso!')


