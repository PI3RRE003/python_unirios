def calcular_media(notas):
    for nome, nota in notas.items():
        media = sum(nota)/len(nota)
        print(f'Média dos alunos:\nNome:{nome} - Média:{media}')

def aprovados(media):
    situacao = ''
    for nome, nota in media.items():
        if media >= 7:
            media = sum(nota)/len(nota)
            situacao = 'Aprovado!'
            print(f'\nNome:{nome} - Média:{media:.2f} - Status:{situacao}')

def reprovados(media):
    situacao = ''
    for nome, nota in media.items():
        if media < 7:
            media = sum(nota)/len(nota)
            situacao = 'Reprovado!'
            print(f'\nNome:{nome} - Média:{media:.2f} - Status:{situacao}')
        
aluno = {}
for i in range(1,3):
    nome = input('\nDigite seu nome:')
    nota_1 = float(input('Digite 1 Nota:'))
    nota_2 = float(input('Digite 2 Nota:'))
    nota_3 = float(input('Digite 3 Nota:'))
    aluno[nome] = [nota_1, nota_2, nota_3]

#calcular_media(aluno)
aprovados(aluno)
reprovados(aluno)
