alunos = []
for i in range(1,3):
    print(f'\n{i} aluno:')
    nome = input('Digite o nome:')
    nota_1 = int(input('Digite a 1° nota:'))
    nota_2 = int(input('Digite a 2° nota:'))
    aluno = [nome, nota_1, nota_2]
    alunos.append(aluno)

for aluno in alunos:
    media = (aluno[1] + aluno[2])/2
    situacao = ''
    if media >= 7:
        situacao ='Aprovado'
        print(f'Status:{situacao} - Nome: {aluno[0]} - Média:{media}')
    elif media < 7:
        situacao = 'Reprovado'
        print(f'Status:{situacao} - Nome: {aluno[0]} - Média:{media}')