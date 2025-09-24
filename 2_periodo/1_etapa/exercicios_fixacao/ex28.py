def cadastrar_livro():
    print("\n========= CADASTRAR LIVRO ==========")

    titulo =  input("Digite o titulo do livro: ")
    if verifica_cadastro_titulo(titulo):
        return
    
    autor =  input("Digite o nome do autor: ")
    if verifica_cadastro_autor(autor):
        return
    
    genero =  input("Digite o genero do livro: ")
    if verifica_cadastro_genero(genero):
        return
    
    livro = [titulo, autor,genero]
    livros.append(livro)
    print("\nLIVRO CADASTRADO COM SUCESSO !!!")
    print(f"Livro:{titulo} - Autor:{autor} - Gênero:{genero}")

def verifica_cadastro_titulo(titulo):
    if not titulo.strip():
        print("CAMPO TITULO NÃO PODE ESTAR VAZIO")
        return True

    for livro in livros:
        if livro[0] == titulo:
            print(f"\nERRO:JA EXISTE ESTE TITULO: {livro[0]} - AUTOR: {livro[1]}")
            return True
    return False

def verifica_cadastro_autor(autor):
    if not autor.strip():
        print("\nCAMPO AUTOR NÃO PODE SER VAZIA!!!")
        return True
    return False

def verifica_cadastro_genero(genero):
    if not genero.strip():
        print("CAMPO GENERO NÃO PODE ESTAR VAZIO")
        return True
    return False



def listar_todos_livros():
    print("\n=========== LISTA DE LIVROS ===========")
    encontrado = False
    for livro in livros:
        encontrado = True
        print(f"Livro:{livro[0]} - Autor:{livro[1]} - Gênero:{livro[2]}")
        return True

    if encontrado == False:
        print("\n----- Lista de livros vazia ------")

def buscar_livro_por_autor():
    print("\n========== LIVROS POR AUTOR =========")
    encontrado = False
    autor = input("Digite o nome do autor: ")
    for livro in livros:
        if livro[1] == autor:
            encontrado = True
            print(f"Livro:{livro[0]} - Autor:{livro[1]} - Gênero:{livro[2]}")
            return True

    if encontrado == False:
        print("\n----- Lista de livros vazia ------")

def listar_por_genero():
    print("========== LIVROS POR GENERO =========")
    encontrado = False
    genero = input("Digite um genero: ")
    for livro in livros:
        if livro[2] == genero:
            encontrado = True
            print(f"Livro:{livro[0]} - Autor:{livro[1]} - Gênero:{livro[2]}")
            return True

    if encontrado == False:
        print("\n----- Lista de livros vazia ------")


livros = []
def menu():
    while True:
        print("\n========== GERENCIAMENTO DE LIVROS ==========")
        print("1 - Cadastrar um livro\
            \n2 - Listar todos os livros\
            \n3 - Buscar por autor\
            \n4 - Listar por genero\
            \n0 - Sair")
        
        op = int(input("Digite uma opção:"))

        if op == 1:
            cadastrar_livro()
        elif op == 2:
            listar_todos_livros()
        elif op == 3:
            buscar_livro_por_autor()
        elif op == 4:
            listar_por_genero()
        elif op == 0:
            print("Encerrando o programa.....")
            break

menu()