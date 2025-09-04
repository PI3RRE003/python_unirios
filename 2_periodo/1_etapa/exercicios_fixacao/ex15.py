def resultado(alunos,notas):
        media = sum(notas)/len(notas)
        situacao = ''
        for aluno in alunos:
              if media >=7:
                    situacao = 'APROVADOS'
                    print(f'{situacao}:')
                    print(f'\nAluno:{aluno} - Média:{media}')
              else:
                    situacao = 'REPROVADO'
                    print(f'\nAluno:{aluno} - Média:{media} - Situação{situacao}')


alunos = {}
for i in range(1,3):
    aluno = input('\nDigite o nome do aluno: ')
    nota_1 = float(input('Digite 1 nota: '))
    nota_2 = float(input('Digite 2 nota: '))
    nota_3 = float(input('Digite 3 nota: '))
    
    notas = [nota_1, nota_2, nota_3]
    alunos[aluno] = notas

resultado(alunos, notas)