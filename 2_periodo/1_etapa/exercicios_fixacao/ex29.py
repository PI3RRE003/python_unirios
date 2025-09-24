def adicionar_contato():
    print("\n=============== ADICIONAR CONTATO ===============")
    
    nome = input("Digite o nome do contato: ")
    if verifica_contato_nome(nome):
        return
    
    telefone = input("Digite o telefone: ")
    if verifica_contato_telefone(telefone):
        return

    email = input("Digite o email: ")
    contato = {
        'nome' : nome,
        'telefone' : telefone,
        'email' : email
    }

    agenda.append(contato)
    print(f"{nome} adicionado a agenda")
    print("=================================================")

def verifica_contato_nome(nome):
    if not nome.strip():
        print("CAMPO NOME NÃO PODE SER VAZIO")
        return True

    if not isinstance(nome, str):
        print("CAMPO NOME DEVE CONTER LETRAS")
        return True
    
def verifica_contato_telefone(telefone):
    if not telefone.strip():
        print("CAMPO TELEFONE NÃO PODE SER VAZIO")
        return True
    
    if len(telefone) < 9:
        print("CAMPO TELEFONE DEVE TER 9 DIGITOS")
        return True
    

def listar_todos_contatos():
    print("\n=============== LISTA DE CONATOS ===============")
    for contato in agenda:
        print(f"\nNome: {contato['nome']} - Telefone: {contato['telefone']} - Email: {contato['email']} ")
        return True
    print(f"Nenhum contato a sua lista, adicione")
    print("=================================================")

def buscar_por_nome():
    print("\n=============== LISTA DE CONATOS ===============")
    nome = input("Digite o nome do contato: ")
    for contato in agenda:
        if contato['nome'] == nome:
            print(f"\nNome: {contato['nome']} - Telefone: {contato['telefone']} - Email: {contato['email']} ")
            return True
    print(f"Nenhum contato com esse nome, tente novamente")
    print("=================================================")

def alterar_contato():
    print("\n=============== ALTERAR CONATO ===============")
    for contato in agenda:
            print(f"\nNome: {contato['nome']} - Telefone: {contato['telefone']} - Email: {contato['email']} ")

    nome = input("Digite o nome do contato que deseja alterar: ")
    if contato['nome'] == nome:
        nome_atualizado = input("Digite o nome atualizado: ")
        if verifica_contato_nome(nome_atualizado):
            return
        contato['nome'] = nome_atualizado

        telefone = input("Digite o telefone atualizado: ")
        if verifica_contato_telefone(telefone):
            return
        contato['telefone'] = telefone
        
        email = input("Digite o email atualizado: ")
        contato['email'] = email
        print(f"{contato['nome']} atualizado com sucesso !!!")
        print("=================================================")


def remover_contato():
    print("\n=============== REMOVER CONATO ===============")
    for contato in agenda:
            print(f"\nNome: {contato['nome']} - Telefone: {contato['telefone']} - Email: {contato['email']} ")
    
    nome = input("Digite o nome do contato que deseja remover: ")
    if verifica_contato_nome(nome):
        return
    for contato in agenda:
        if contato['nome'] == nome:
            agenda.remove(contato)
            print(f"{contato['nome']} removido com sucesso") 
    print("=================================================")


agenda = []
def menu():
    while True:
        print("\n=============== LISTA DE CONTATOS ===============")
        print("1 - Adicionar contato\
            \n2 - Listar todos os contatos\
            \n3 - Buscar contato por nome\
            \n4 - Alterar contato\
            \n5 - Remover contato\
            \n0 - Sair\
            \n=================================================")
        
        op = int(input("Digite a opção: "))

        if op == 1:
            adicionar_contato()
        elif op == 2:
            listar_todos_contatos()
        elif op == 3:
            buscar_por_nome()
        elif op == 4:
            alterar_contato()
        elif op == 5:
            remover_contato()
        elif op == 0:
            print("\nFECHANDO AGENDA")
            break
    
menu()