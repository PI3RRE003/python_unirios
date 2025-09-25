from datetime import datetime

livros = []

def registrar_livros():
    print("\n========= REGISTRAR LIVRO ==========")
    isbn = "00" + str(gerar_codigo_isbn())

    titulo = input("Digite o titulo do livro: ")
    if verifica_titulo_livro(titulo):
        return
    
    autor = input("Digite o autor do livro: ")
    if verifica_autor_livro(autor):
        return
    
    genero = input("Digite o genero do livro: ")
    if verifica_genero_livro(genero):
        return
    
    livro = [isbn,titulo,autor,genero]
    livros.append(livro)
    print("\nLIVRO CADASTRADO COM SUCESSO")
    print(f"ISBN:{livro[0]} - TITLULO:{livro[1]} - AUTOR:{livro[2]} - GENERO:{livro[3]}")


def gerar_codigo_isbn():
    if len(livros) == 0:
        isbn = 1
    else:
        isbn = len(livros)+1
    return isbn

def verifica_titulo_livro(titulo):
    if len(titulo) == 0:
        print("ERRO: titulo não pode ser vazio")
        return True
    return False

def verifica_autor_livro(autor):
    if len(autor) == 0:
        print("ERRO: autor não pode ser vazio")
        return True
    return False

def verifica_genero_livro(genero):
    if len(genero) == 0:
        print("ERRO: genero não pode ser vazio")
        return True
    return False



def buscar_por_isbn(isbn):

    verifica_lista_livros()

    print("\n========== BSUCAR LIVRO POR ISBN ==========")
    for livro in livros:
        if livro[0] == isbn:
            print(f"ISBN:{livro[0]} - TITLULO:{livro[1]} - AUTOR:{livro[2]} - GENERO:{livro[3]}")

def listar_todos_livros():
    
    verifica_lista_livros()
    print("\n========= LISTANDO TODOS OS LIVROS =========")
    for livro in livros:
        print(f"ISBN:{livro[0]} - TITLULO:{livro[1]} - AUTOR:{livro[2]} - GENERO:{livro[3]}")

def verifica_lista_livros():
    if len(livros) == 0:
        print("\nLISTA DE LIVROS VAZIA !!!")
        op = input("Deseja adicionar? (S/N): ")
        if op == 'S' or op == 's':
            return registrar_livros()
        else:
            print("\nRetornando ao menu de livros")
            return


usuarios = []

def registrar_usuarios():
    print("\n========= REGISTRANDO USUARIO ==========")
    codigo = "00" + str(gerar_codigo_usuario())
    
    nome = input("Digite o nome do usuario: ")
    if verifica_nome_usuario:
        return
    
    telefone = input("Digite o telefone do usuario: ")
    if verifica_telefone_usuario:
        return
    
    usuario = [codigo, nome,telefone]
    usuarios.append(usuario)
    print("\nUSUARIO CADASTRADO COM SUCESSO !!!")
    print(f"Codigo:{usuario[0]} - Nome:{usuario[1]} - Telefone:{usuario[2]}")
    

def gerar_codigo_usuario():
    if len(usuarios) == 0:
        codigo = 1
    else:
        codigo = len(usuarios)+1
    return codigo

def verifica_nome_usuario(nome):
    if len(nome) == 0:
        print("ERRO: nome não pode ser vazio")
        return True
    return False

def verifica_telefone_usuario(telefone):
    if len(telefone) == 0:
        print("ERRO: telefone não pode ser vazio")
        return True
    return False

def verifica_lista_usuarios():
    if len(usuarios) == 0:
        print("\nLISTA DE USUARIOS VAZIA !!!")
        op = input("Deseja adicionar? (S/N): ")
        if op == 'S' or op == 's':
            return registrar_usuarios()
        else:
            print("\nRetornando ao menu de usuarios")
            return

def buscar_por_codigo(codigo):
    
    verifica_lista_usuarios()
    
    print("\n========== BUSCANDO USUARIO POR CODIGO =========")
    for usuario in usuarios:
        if usuario[0] == codigo:
            print(f"Codigo:{usuario[0]} - Nome:{usuario[1]} - Telefone:{usuario[2]}")

def listar_todos_usuarios():
    
    verifica_lista_usuarios()

    print("\n========== LISTANDO TODOS USUARIOS ==========")
    for usuario in usuarios:
        print(f"Codigo:{usuario[0]} - Nome:{usuario[1]} - Telefone:{usuario[2]}")

emprestimos = []

def realizar_emprestimos():
    print("\n========== REALIZANDO EMPRESTIMO ==========")
    
    codigo_isbn = input("Digite o codigo ISBN: ")
    if validar_isbn(codigo_isbn):
        return
    
    codigo_usuario = input("Digite o codigo do usuario: ")
    if validar_codigo_usuario(codigo_usuario):
        return
    
    nome = input("Digite o nome do usuario: ")
    if validar_nome_usuario(nome):
        return
    
    data = datetime.now().strftime("%d/%m/%Y")
    

    emprestimo = [codigo_isbn,codigo_usuario,nome,data]
    emprestimos.append(emprestimo)
    print("\nEMPRESTIMO REALIZADO COM SUCESSO !!!")
    print(f"ISBN:{emprestimo[0]} - CODIGO USUARIO:{emprestimo[1]} NOME:{emprestimo[2]} - DATA:{emprestimo[3]}")

def validar_isbn(isbn):
    for livro in livros:
        if livro[0] == isbn:
            return True
        else:
            print("ERRO: ISBN NÃO EXISTE ADICIONE O LIVRO")
            return verifica_lista_livros()
    
def validar_codigo_usuario(codigo):
    for usuario in usuarios:
        if usuario[0] == codigo:
            return True
        else:
            print("ERRO: USUARIO NÃO ENCONTRADO CADASTRE")
            return verifica_lista_usuarios()

def validar_nome_usuario(nome):
    for usuario in usuarios:
        if usuario[1] == nome:
            return True
        else:
            print("ERRO: USUARIO NÃO ENCONTRADO CADASTRE")
            return verifica_lista_usuarios()
        
def verifica_lista_emrpestimos():
    if len(emprestimos) == 0:
        print("\nLISTA DE EMPRESTIMOS VAZIA !!!")
        op = input("Deseja adicionar? (S/N): ")
        if op == 'S' or op == 's':
            return realizar_emprestimos()
        else:
            print("\nRetornando ao menu de usuarios")
            return

def listar_todos_emprestimos():
    
    verifica_lista_emrpestimos()

    print("\n========= LISTANDO EMPRESTIMOS ========")
    for emprestimo in emprestimos:
        print(f"ISBN:{emprestimo[0]} - CODIGO USUARIO:{emprestimo[1]} NOME:{emprestimo[2]} - DATA:{emprestimo[3]}")

def buscar_emprestimo_isbn(isbn):
    
    verifica_lista_emrpestimos()

    print("\n========= BUSCANDO POR ISBN =========")
    for emprestimo in emprestimos:
        if emprestimo[0] == isbn:
            print(f"ISBN:{emprestimo[0]} - CODIGO USUARIO:{emprestimo[1]} NOME:{emprestimo[2]} - DATA:{emprestimo[3]}")
            

