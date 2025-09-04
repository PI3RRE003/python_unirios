def adicionar_aluno():
    print("\n========== ADICIONAR ALUNO ==========")
    nome = input('Digite o nome do aluno: ')
    cpf = input('Digite o CPF: ')
    
    if verifica_cpf(cpf):
        print(f'ERRO: O CPF {cpf} já está cadastrado!')
        return 
    
    aluno = [nome, cpf]
    alunos.append(aluno)
    print(f"{nome} adicionado a db ")
    

def verifica_cpf(cpf):
    for aluno in alunos:
        if aluno[1] == cpf:
            return True
    return False



def adicionar_notas():
    print("\n========== ADICIONAR NOTAS DO ALUNO ==========")
    nome = input('Digite o nome do aluno que deseja adicionar a nota: ')
    aluno_encontrado = False
    for aluno in alunos:
        print(aluno)
        if nome == aluno[0]:
            
            nota_1 = float(input('Digite a 1 Nota: '))
            nota_2 = float(input('Digite a 2 Nota: '))
            nota_3 = float(input('Digite a 3 Nota: '))
            notas = [nota_1, nota_2, nota_3]
            if len(aluno) > 2:
                aluno[2] = notas
            else:
                aluno.append(notas)
            
            print(f'Notas de {nome} adicionadas com sucesso {notas}')
            aluno_encontrado = True
            break
    
    if not aluno_encontrado:
        print('Erro aluno não encontrado')


    
    
def calcular_media_aluno():
    print("\n========== CALCULAR MÉDIA DO ALUNO ==========")
    nome = input('Digite o nome do aluno que deseja calcular a média: ')
    aluno_encontrado = False
    for aluno in alunos:
        print(aluno)
        if nome == aluno[0]:
            if len(aluno) < 3:
                print("aluno não contem notas cadastradas")
            else:
                somar_notas = sum(aluno[2])
                media = somar_notas / len(aluno[2])
                print(f'A média de {nome} é {media:.2f}')

            aluno_encontrado = True
            break

    if not aluno_encontrado:
        print(f"ERRO aluno {nome} não encontrado")       
    
def exibir_boletim_da_turma():
    print("\n========== BOLETIM DA TURMA ==========")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        if len(aluno) > 2:
            soma_notas = sum(aluno[2])
            media = soma_notas / len(aluno[2])
            situacao = "Aprovado" if media >= 7 else "Reprovado"
            print(f"Aluno: {aluno[0]} | CPF: {aluno[1]} | Média: {media:.2f} | Situação: {situacao}")
        else:
            print(f"Aluno: {aluno[0]} | CPF: {aluno[1]} | Média: Sem notas.")

alunos = []
def menu():
    while True:
        print("\n========== GERENCIAMENTO DE ALUNOS ==========")
        print("1 - Adicionar Aluno\
             \n2 - Adicionar Notas\
             \n3 - Calcular Média do Aluno\
             \n4 - Exibir Boletim da turma\
             \n5 - Sair")
        
        op = int(input('Digite a opção: '))

        if op == 1:
            adicionar_aluno()
        elif op ==2:
            adicionar_notas()
        elif op == 3:
            calcular_media_aluno()
        elif op == 4:
            exibir_boletim_da_turma()
        elif op == 0:
            print('Encerrando o programa....')
            break

menu()
