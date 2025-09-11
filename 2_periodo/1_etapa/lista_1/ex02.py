def cadastrar_aluno():
    nome = input('Digite o nome do aluno: ')
    try:
        nota_1 = float(input('Digite 1 nota do aluno: '))
        nota_2 = float(input('Digite 2 nota do aluno: '))
        nota_3 = float(input('Digite 3 nota do aluno: '))
    except ValueError:
        print('Erro: Nota inválida. Tente novamente.')
        op = input('Deseja tentar cadastrar novamente? (S/N):')
        if op == 'S' or op == 's':
            return cadastrar_aluno()
        elif op == 'N' or op == 'n':
            print('Voltando ao menu principal...')
            return
    else:
        aluno = [nome, nota_1, nota_2, nota_3]
        alunos.append(aluno)
        print(f'Aluno {nome} cadastrado com sucesso!')

def calcular_media():
    print('\n========== CÁLCULO DE MÉDIA ==========')
    if not alunos:
        print('Nenhum aluno cadastrado.')
        op = input('Deseja cadastrar ? (S/N):')
        if op == 'S' or op == 's':
            return cadastrar_aluno()
        elif op == 'N' or op == 'n':
            print('Voltando ao menu principal...')
            return

    else:
        print('SELECIONE UM ALUNO PARA CALCULAR A MÉDIA:')
        for aluno in alunos:
            print(f'Aluno: {aluno[0]}')

        nome = input('Digite o nome do aluno: ')
        for aluno in alunos:
            if aluno[0] == nome:
                media = sum(aluno[1:]) / 3
                print(f'\nA média do aluno {nome} é: {media:.2f}')
                return
        print('Aluno não encontrado.')

def situacao_aluno():
    print('\n========== SITUAÇÃO DO ALUNO ==========')
    if not alunos:
        print('Nenhum aluno cadastrado.')
        op = input('Deseja cadastrar ? (S/N):')
        if op == 'S' or op == 's':
            return cadastrar_aluno()
        elif op == 'N' or op == 'n':
            print('Voltando ao menu principal...')
            return

    else:
        for aluno in alunos:
            print(aluno)
        nome = input('Digite o nome do aluno: ')
        for aluno in alunos:
            if aluno[0] == nome:
                media = sum(aluno[1:]) / 3
                if media >= 7:
                    situacao = 'Aprovado'
                elif 5 <= media < 7:
                    situacao = 'Recuperação'
                else:
                    situacao = 'Reprovado'
                print(f'O aluno {nome} está: {situacao} com média {media:.2f}')
                return
        print('Aluno não encontrado.')

alunos = []
def menu():
    while True:
        print('\n========= GERENCIAMENTO DE ALUNOS ==========')
        print('1 - Cadastrar aluno')
        print('2 - Calular média')
        print('3 - Situação aluno')
        print('0 - Sair')
        print('=============================================')
        
        op = int(input('Digite a opção desejada: '))

        if op == 1:
            cadastrar_aluno()
        elif op == 2:
            calcular_media()
        elif op == 3:
            situacao_aluno()
        elif op == 0:
            print('Encerrando o programa...')
            break

menu()