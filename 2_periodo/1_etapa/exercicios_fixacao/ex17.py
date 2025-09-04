alunos = []

def mostrar_turma():
        for aluno in alunos:
            return f'\nAlunos:\nNotas: {aluno[0]} - {aluno[1]} - {aluno[2]} - {aluno[3]}'

def calcula_media_nota():
    for nota in alunos:
        media = (nota[1] + nota[2] + nota[3])/3
    return f'\nMédia da sala:{media:.2f}\n'

def alunos_acima_media():
    for aluno in alunos:
        media = (aluno[1] + aluno[2] + aluno[3])/3
        situacao = ''
        if media > 7:
            situacao ='Aprovado'
            return (f'Status:{situacao} - Nome: {aluno[0]} - Média:{media}')
        elif media < 7:
            situacao = 'Reprovado'
            return (f'Status:{situacao} - Nome: {aluno[0]} - Média:{media}')    
def menu():
    for i in range(1,2):
        print(f'{i} Aluno:')
        nome = input('Digite o nome do aluno: ')
        nota_1 = float(input('Digite 1 nota: '))
        nota_2 = float(input('Digite 2 nota: '))
        nota_3 = float(input('Digite 3 nota: '))
        aluno = [nome,nota_1,nota_2,nota_3]
        alunos.append(aluno)
        



menu()
print(mostrar_turma())
print(calcula_media_nota())
print(alunos_acima_media())