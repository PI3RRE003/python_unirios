def cadastrar_eleitor():
    print('\n========== CADASTRAR ELEITOR ========')
    nome = input('Digite o nome do eleitor: ')
    cidade = input('Digite a cidade do eleitor: ')
    titulo = input('Digite o título de eleitor: ')
    if not titulo:
        print(f'Erro ao cadastrar eleitor, Motivo: titulo em branco')
        return
    else:
        for eleitor in eleitores:
            if eleitor[1] == titulo:
                print(f'Erro ao cadastrar eleitor, Motivo: Título {titulo} já cadastrado para o eleitor {eleitor[0]}')
                return
            
    eleitor = [nome, titulo, cidade]
    eleitores.append(eleitor)
    print(f'Eleitor: {nome} cadastrado com sucesso!')

def listar_eleitor_cadastrado():
    print('========== ELEITORES CADASTRADOS ==========')
    if not eleitores:
        print('Nenhum eleitor cadastrado.')
        op = input('Deseja cadastrar? (S/N):')
        if op == 'S' or op == 's':
            return cadastrar_eleitor()
        elif op == 'N' or op == 'n':
            print('Voltando ao menu principal...')
            return
    else:
        for eleitor in eleitores:
            print(f'Nome: {eleitor[0]}, Título: {eleitor[1]}, Cidade: {eleitor[2]}')

def listar_eleitor_cidade():
    print('========== LISTAR ELEITORES POR CIDADE ==========')
    if not eleitores:
        print('Nenhum eleitor cadastrado.')
        op = input('Deseja cadastrar? (S/N):')
        if op == 'S' or op == 's':
            return cadastrar_eleitor()
        elif op == 'N' or op == 'n':
            print('Voltando ao menu principal...')
            return
    else:
        cidade = input('Digite o nome da cidade: ')
        for eleitor in eleitores:
            if eleitor[2] == cidade.lower():
                print(f'Nome: {eleitor[0]}, Título: {eleitor[1]}, Cidade: {eleitor[2]}')
            else:
                print('Nenhum eleitor encontrado nesta cidade.')
                return

def buscar_eleitor_titulo():
    print('========== BUSCAR ELEITOR POR TÍTULO ==========')
    if not eleitores:
        print('Nenhum eleitor cadastrado.')
        op = input('Deseja cadastrar? (S/N):')
        if op == 'S' or op == 's':
            return cadastrar_eleitor()
        elif op == 'N' or op == 'n':
            print('Voltando ao menu principal...')
            return
    else:
        titulo = input('Digite o título de eleitor: ')
        for eleitor in eleitores:
            if eleitor[1] == titulo:
                print(f'Nome: {eleitor[0]}, Título: {eleitor[1]}, Cidade: {eleitor[2]}')
                return
            else:
                print('Eleitor não encontrado.')
                return

eleitores = []
def menu():
    while True:
        print('\n========= CADASTRO DE ELEITORES ==========')
        print('1 - Cadastrar eleitor')
        print('2 - Listar eleitores cadastrados')
        print('3 - Listar eleitor por cidade')
        print('4 - Buscar eleitor por titulo')
        print('0 - Sair')
        print('==========================================')

        op = int(input('Digite a opção desejada: '))

        if op == 1:
            cadastrar_eleitor()
        elif op == 2:
            listar_eleitor_cadastrado()
        elif op == 3:
            listar_eleitor_cidade()
        elif op == 4:
            buscar_eleitor_titulo()
        elif op == 0:
            print('Encerrando o programa...')
            break
menu()
