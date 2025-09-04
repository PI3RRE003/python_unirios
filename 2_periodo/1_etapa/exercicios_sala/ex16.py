def media_aluno(nota_1,nota_2):
    media = nota_1 + nota_2 / 2
    if media > 7:
        return 'Aprovado na média'
    elif media > 3 and media < 6.9:
        return 'Final'
    elif media < 3:
        return 'Reprovado'
    

nota_1 = int(input('Digite sua 1 nota: '))
nota_2 = int(input('Digite sua 2 nota: '))
print(media_aluno(nota_1,nota_2))
