from _datetime import  *
biblioteca = []
def cadastrar_livro():
    print("\n====== CADASTRANDO LIVRO ======")
    try:
        codigo =  "00" + str(gerar_codigo())

        titulo = input("Digite o titulo do livro: ")
        if titulo == '':
            print("Titulo não pode ser vazio")
            return

        autor = input("Digite o nome do autor: ")
        if autor == '':
            print("Autor não pode ser vazio")
            return

        quantidade_exemplar = int(input("Digite a quantidade de exemplares: "))
        if quantidade_exemplar <= 0:
            print("Quantidade deve ser positiva")
            return

        livro = {
            "CODIGO" : codigo,
            "TITULO" : titulo,
            "AUTOR" : autor,
            "QUANTIDADE" : quantidade_exemplar
        }
        biblioteca.append(livro)
        print(f"\nLivro cadastrado com sucesso !"
              f"\nCodigo:{livro['CODIGO']}"
              f"\nTitulo:{livro['TITULO']}"
              f"\nAutor:{livro['AUTOR']}"
              f"\nQuantidade:{livro['QUANTIDADE']}")

    except ValueError:
        print("\nDigite apenas numeros")
    except Exception as e:
        print(f"\nError:{e}")

def gerar_codigo():
    if len(biblioteca) == 0:
        codigo = 1
    else:
        codigo = len(biblioteca)+1
    return codigo

def buscar_livro_pelo_codigo(codigo):
    print("\n====== BUSCANDO LIVRO PELO CODIGO ======")
    try:
        verifica_biblioteca()
        for livro in biblioteca:
            if livro['CODIGO'] == codigo:
                print(f"Livro cadastrado com sucesso !"
                      f"\nCodigo:{livro['CODIGO']}"
                      f"\nTitulo:{livro['TITULO']}"
                      f"\nAutor:{livro['AUTOR']}"
                      f"\nQuantidade{livro['QUANTIDADE']}")
            else:
                print("\nLivro não encontrado")
    except Exception as e:
        print(f"\nError:{e}")

def listar_todos_livros_cadastrados():
    print("\n====== LISTANDO TODOS LIVROS ======")
    try:
        verifica_biblioteca()
        for livro in biblioteca:
            print(f"\nCodigo:{livro['CODIGO']}"
                  f"\nTitulo:{livro['TITULO']}"
                  f"\nAutor:{livro['AUTOR']}"
                  f"\nQuantidade{livro['QUANTIDADE']}")
    except Exception as e:
        print(f"\nError:{e}")

def controlar_quantidade_exemplar(codigo):
    print("\n====== CONTROLANDO ESTOQUE EXEMPLAR ======")
    try:
        verifica_biblioteca()
        for livro in biblioteca:
            if livro['CODIGO'] == codigo:
                print(f"\nCodigo:{livro['CODIGO']}"
                      f"\nTitulo:{livro['TITULO']}"
                      f"\nAutor:{livro['AUTOR']}"
                      f"\nQuantidade{livro['QUANTIDADE']}")

                op = int(input("\nDigite a opção:"
                           "\n1 - Adicionar exemplar"
                           "\n2 - Remover exempar"
                           "\n0 - sair"))
                if op == 1:
                    op1 = int(input(f"\nDigite a quantidade de exemplares que deseja adicionar do livro {livro['TITULO']}"))
                    if op1 <= 0:
                        print("\nError quantidade deve ser positiva")
                        return
                    else:
                        livro['QUANTIDADE'] += op1
                        print(f"\nLivro:{livro['TITULO']} atualizado a quantidade: {livro['QUANTIDADE']}")
                elif op == 2:
                    op2 = int(input(f"Digite a quantidade de exemplares que deseja remover do livro {livro['TITULO']}"))
                    if op2 <= 0:
                        print("\nError quantidade deve ser positiva")
                        return
                    else:
                        livro['QUANTIDADE'] -= op2
                        print(f"\nLivro:{livro['TITULO']} atualizado a quantidade: {livro['QUANTIDADE']}")
                elif op == 0:
                    print("\nretornando ao menu...")
                    return
                else:
                    print("\nDigite apenas de 0 a 2")
            else:
                print("\nLivro não encontrado")
    except Exception as e:
        print(f"\nError:{e}")

def verifica_biblioteca():
    if len(biblioteca) == 0:
        print("\nBiblioteca vazia, adicione um livro")
        op = int(input("\nDeseja adicionar?"
                       "\n1 - Sim"
                       "\n2 - Não"))
        if op == 1:
            print("\nDirecionando para cadastro de livro")
            return cadastrar_livro()
        elif op == 2:
            print("\nRetornando ao menu principal...")
            return
    else:
        pass

emprestimos = []

def realizar_emprestimo(codigo):
    print("\n====== REALIZANDO EMPRESTIMO DE EXEMPLAR ======")
    try:
        livro = buscar_livro_pelo_codigo(codigo)
        if livro is not None:
            print("Livro não encontrado")
        else:
            codigo_emprestimo = "00" + str(gerar_codigo())
            data = date.today()
            titulo = livro['TITULO']
            vencimento = data + timedelta(days=15)

            emprestimo = {
            "CODIGO" : codigo_emprestimo,
            "DATA" : data,
            "LIVRO" : titulo,
            "VENCIMENTO" : vencimento
        }
        emprestimos.append(emprestimo)
        print(f"\nEmprestimo realizado com sucesso !"
              f"\nCodigo:{emprestimo['CODIGO']}"
              f"\nData:{emprestimo['DATA']}"
              f"\nLivro:{emprestimo['LIVRO']}"
              f"\nVencimento:{emprestimo['VENCIMENTO']}")
    except Exception as e:
        print(f"\nError:{e}")

def listar_todos_emprestimos():
    print("\n====== LISTANDO TODOS EMPRESTIMOS ======")
    try:
        for emprestimo in emprestimos:
            print(f"\nCodigo:{emprestimo['CODIGO']}"
                  f"\nData:{emprestimo['DATA']}"
                  f"\nLivro:{emprestimo['LIVRO']}"
                  f"\nVencimento:{emprestimo['VENCIMENTO']}")
    except Exception as e:
        print(f"\nError:{e}")

def buscar_emprestimo_pelo_codigo(codigo):
    print("\n====== BUSCANDO EMPRESTIMO PELO CODIGO ======")
    try:
        for emprestimo in emprestimos:
            if emprestimo['CODIGO'] == codigo:
                print(f"\nCodigo:{emprestimo['CODIGO']}"
                      f"\nData:{emprestimo['DATA']}"
                      f"\nLivro:{emprestimo['LIVRO']}"
                      f"\nVencimento:{emprestimo['VENCIMENTO']}")
            else:
                print("\nEmprestimo não encontrado")
    except Exception as e:
        print(f"\nError:{e}")

def verifa_emprestimos():
    if len(emprestimos) == 0:
        print("\nEmprestimos vazios, adicione")
        op = int(input("\nDeseja adicionar?"
                       "\n1 - Sim"
                       "\n2 - Não"))
        if op == 1:
            print("\nDirecionando para cadastro de emprestimo")
            return realizar_emprestimo()
        elif op == 2:
            print("\nRetornando ao menu principal...")
            return
    else:
        pass
