alunos = []
while True:
    print('\n1 - cadastrar aluno')
    print('2 - Buscar aluno')#add cpf
    print('3 - Listar alunos')
    print('4 - Buscar por CPF')#buscar pelo cpf
    print('5 - Deletar Aluno')
    print('0 - Sair')

    op = int(input('Digite uma opção: '))

    if op == 1:
        print('\n----Cadastrar Aluno----')
        nome = input('Digite o nome do aluno: ')
        idade = int(input('Digite idade do aluno: '))
        nome_curso = input('Digite o curso do aluno: ')
        cpf = input('Digite cpf aluno: ')
        print('\nAluno cadastrado com sucesso!\n')
        aluno = [nome,idade,nome_curso,cpf]
        alunos.append(aluno)
    elif op == 2:
        print('\n''---Buscar aluno---')
        nome = input('Digite o nome do aluno: ')
        encontrado = False
        for aluno in alunos:
            if aluno[0] == nome:
                print('\nAluno encontrado!')
                print(f'Nome:{aluno[0]} - Idade:{aluno[1]} - Curso:{aluno[2]}\n')
                encontrado = True
        if encontrado == False:
            print('\nAluno não cadastrado!\n')
    elif op == 3:
        print('---Listar alunos---')
        for aluno in alunos:
            print(aluno)
    elif op == 4:
        print('\n''---Buscar aluno pelo CPF---')
        cpf = input('Digite o CPF:')
        encontrado = False
        for aluno in alunos:
            if aluno[3] == cpf:
                print('\nAluno encontrado pelo CPF!')
                print(f'CPF:{aluno[3]} - Nome:{aluno[0]} - Idade:{aluno[1]} - Curso:{aluno[2]}\n')
                encontrado = True
        if encontrado == False:
            print('CPF não encontrado')
    elif op == 5:
        print('\n--- Lista de alunos ---')
        for i, aluno in enumerate(alunos, start=1):
            print(f'Indice: {i} - Aluno: {aluno[0]} - Idade:{aluno[1]} - Curso:{aluno[2]} - CPF:{aluno[3]}')
            removido = False
            remover = int(input('\nDigite qual aluno deseja remover pelo indice:'))
            if remover == len(alunos):
                removido = True
                alunos.remove(aluno)
                print(f'DELETADO COM SUCESSO:(Indice: {i} - Aluno: {aluno[0]} - Idade:{aluno[1]} - Curso:{aluno[2]} - CPF:{aluno[3]})')
            else:
                removido = False
                print('Erro')     
    elif op == 0:
        print('Encerrando....')
        break