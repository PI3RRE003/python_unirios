def mostrar_nota_aluno():
    if not alunos:
        print('LISTA VAZIA, ADICIONE ALUNOS NA (OPÇÃO 4) ')
    else:
        for aluno in alunos:
            print(aluno)
        

def calcular_media():
    print('\n========== CALCULA MEDIA ==========')
    if not alunos:
        print('LISTA VAZIA, ADICIONE ALUNOS NA (OPÇÃO 4) ')
    else:
        for aluno in alunos:
            print(aluno)

    nome = input('Digite o nome do aluno: ')
    for aluno in alunos:
      if nome == aluno[0]:
          media = (aluno[1] + aluno[2] + aluno[3]) / 3
          aluno.append(media)
          print(f'Aluno: {nome} - Média: {media:.2f}')

def situacao_aluno():
    print('=========== SITUAÇÃO DO ALUNO ==========')
    if not alunos:
        print('LISTA VAZIA, ADICIONE ALUNOS NA (OPÇÃO 4) ')
    else:
        for aluno in alunos:
            print(aluno)

    try:
        situacao = ''
        media = aluno[4]
    except:
        print('CALCULE A MÉDIA PARA VER A SITUAÇÃO DO ALUNO')
        return menu()
    
    nome = input('Digite o nome do aluno para saber a situação: ')
    for aluno in alunos:
        if nome == aluno[0]:
            if aluno[4] >= 7:
                situacao = 'aprovado(a)'
            else:
                situacao = 'reprovado ou final'
            
            print(f'Nome:{nome} - Média:{media:.2f} - Situação:{situacao}')

def adicionar_aluno():
    print('========== ADICIONAR ALUNO ==========')
    nome = input('Digite seu nome: ')
    try:
        nota_1 = float(input('Digite a 1 nota: '))
        nota_2 = float(input('Digite a 2 nota: '))
        nota_3 = float(input('Digite a 3 nota: '))
    except ValueError:
        print('Apenas numeros em notas')
    else:    
        aluno = [nome, nota_1,nota_2,nota_3]
        alunos.append(aluno)

alunos = []
def menu():
    while True:
        print('\n========== GERENCIAMENTO DE ALUNOS ==========')
        print('[1] Mostrar nota do aluno')
        print('[2] Calcular a media')
        print('[3] Situação do aluno')
        print('[4] Adicionar Aluno')
        print('[0] Sair')

        op = int(input('Digite sua opção: '))

        if op == 1:
            mostrar_nota_aluno()
        elif op == 2:
            calcular_media()
        elif op == 3:
            situacao_aluno()
        elif op == 4:
            adicionar_aluno()
        elif op == 0:
            print('Encerrando o programa....')
            break
            
menu()