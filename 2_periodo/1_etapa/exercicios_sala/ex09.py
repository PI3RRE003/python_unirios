'''alunos = [
    ['Vitor', 23, 'Sistemas de Informação'],
    ['Kawane', 20, 'Sistemas de Informação'],
    ['Abel', 25, 'Sistemas de Informação'],
]'''
'''
DADOS DE VITOR
print(alunos[0][0])
print(alunos[0][1])
print(alunos[0][2])
'''

alunos = [
    ['Daniel', 8.0, 9.0],
    ['Caua', 10.0, 10.0],
    ['Taina',8.0, 9.0],
]

for aluno in alunos:
    situacao = ''
    media = (aluno[1] + aluno[2])/2
    if media >= 7:
        situacao = 'Aprovado'
    elif media < 7:
        situacao = 'reprovado'

    print(f"aluno:{aluno[0]} - Média:{media} - Situação:{situacao}")

'''
PERCORRE TODAS AS LISTAS DENTRO DA LISTA
for aluno in alunos:
    print(f'Aluno: {alunos.index(aluno)+1}')
    print(f'Nome: {aluno[0]} - Idade: {aluno[1]} - Curso: {aluno[2]}\n')

'''
