alunos = []
def cadastrar():
    print('\n---------- Cadastrar Aluno ---------')
    cpf = input('CPF: ')
    if buscar_pelo_cpf(cpf):
        print('Aluno já existe')
        return
    else:
        nome = input('Nome: ')
        telefone = input('telefone: ')
        aluno = [nome,cpf,telefone]
        alunos.append(aluno)
        print(f'\nAluno:{aluno} cadastrado com sucesso!')

def buscar_nome():
    print('\n-------- Buscar aluno pelo nome --------')
    
    nome = input('Nome: ')
    encontrado = False
    
    for aluno in alunos:
        if nome == aluno[0]:
            print(f'\nAluno encontrado:\nNome:{aluno[0]}\nCPF:{aluno[1]}\nTelefone:{aluno[2]} ')
            encontrado = True
        
        if encontrado == False:
            print('Aluno não encontrado')

def listar_todos():
    print('---------- Todos os alunos ----------')
    if len(alunos) == 0:
        print('Nenhum aluno cadastrado')
    else:
        for aluno in alunos:
            print(aluno)

def buscar_pelo_cpf(cpf) -> None:
    print('---------- Buscar pelo cpf ----------')
    
    #cpf = input('Digite o CPF:')
    encontrado = False

    for i in alunos:
        if cpf == i[1]:
            encontrado = True
            print(f'\nAluno encontrado pelo cpf:\nNome:{i[0]}\nCPF:{i[1]}\nTelefone:{i[2]}')
            return True
        
    if encontrado == False:
        print('CPF NÂO ENCONTRADO NA BASE')
        return False

def main() -> None:
    while True:
        print('\n========== MENU ==========')
        print('1 - CADASTRAR ALUNO\
               \n2 - BUSCAR PELO NOME\
               \n3 - LISTAR ALUNO\
               \n4 - BUSCAR PELO CPF')
        operador = int(input('Digite a opção desejada: '))

        if operador == 1:
            cadastrar()
        elif operador == 2:
            buscar_nome()
        elif operador == 3:
            listar_todos()
        elif operador == 4:
            cpf = input('CPF:')
            buscar_pelo_cpf(cpf)
        elif operador == 0:
            print('Encerrando programa...')
            break
        else:
            print('Opção inválida')
        

main()