"""
Lista de listas e seus indices
"""
#salas = [
#    ['Maria', 'Helena',],
#    ['Elaine',],
#    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],
#]
#print(salas[0][1])#acessar valores dentro da lista
#print(salas[2][1])
#print(salas[2][3][3])


salas = [
    ['Maria', 'Helena',],
    ['Elaine',],
    ['Luiz', 'João', 'Eduarda',],
]

for sala in salas:
    print(f'A sala é {sala} ')
    for aluno in sala:
        print(aluno)
