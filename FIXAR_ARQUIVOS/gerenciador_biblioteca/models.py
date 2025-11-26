#IMPORTAR OS
#ARQUIVO
#VALIDAÇÃO

#WAR

import os
from datetime import date, timedelta

LIVROS = 'livros.txt'
EMPRESTIMOS = 'emprestimos.txt'

def write_livros():
    try:
        if not os.path.exists(LIVROS):
            with open(LIVROS, 'w'):
                print("\nCriando arquivo dos livros")
        else:
            print("\nCarregando arquivo dos livros")
    except Exception as e:
        print(f"Error:{e}")

def append_livros(titulo,autor,codigo_livro,qtd_exemplares):
    try:
        with open(LIVROS, 'a') as arquivo:
            linha = f"{titulo};{autor};{codigo_livro};{qtd_exemplares}\n"
            arquivo.write(linha)
    except Exception as e:
        print(f"Error:{e}")

def read_livros():
    try:
        with open(LIVROS,'r') as arquivo:
            linhas = arquivo.readlines()

            if len(linhas) == 0:
                print("Lista de livros vazia")
            else:
                for linha in linhas:
                    dados = linha.strip().split(";")
                    print(f"\nTitulo:{dados[0]}"
                          f"\nAutor:{dados[1]}"
                          f"\nCodigo do livro:{dados[2]}"
                          f"\nQuantidade de exemplares:{dados[3]}")
                    return dados
    except Exception as e:
        print(f"Error:{e}")

#=============================================

def cadastrar_livro():
    print("\n===== CADASTRANDO LIVRO ======")
    try:
        write_livros()
        print("\n===== CADASTRANDO LIVRO ======")

        titulo =  input("Digite o titulo do livro: ")
        if len(titulo) == 0:
            print("Campo não pode ser em branco")
            return

        autor =  input("Digite o autor do livro: ")
        if len(autor) == 0:
            print("Campo não pode ser em branco")
            return

        qtd_exemplares = int(input("Digite a quantidade de exemplares: "))
        if qtd_exemplares <= 0:
            print("Error: exemplares não podem ser negativos ou zerado")
            return

        codigo_livro = gerar_codigo_livro()

        append_livros(titulo,autor,codigo_livro,qtd_exemplares)
        print(f"\nLivro:{titulo} cadastrado com sucesso!!!"
              f"\nCodigo do Livro:{codigo_livro}")

    except Exception as e:
        print(f"Error:{e}")


def gerar_codigo_livro():
    try:
        with open(LIVROS, 'r') as arquivo:
            linha = arquivo.readlines()
            codigo_livro = "L00" + str(len(linha)+1)
            return  codigo_livro
    except Exception as e:
        print(f"Error:{e}")


def buscar_livro_pelo_codigo(codigo_livro):
    print("\n===== BUSCANDO LIVRO PELO CODIGO ======")
    try:
        dados = read_livros()
        livro = dados[2]
        if livro == codigo_livro:
            return dados
    except Exception as e:
        print(f"Error:{e}")

def listar_todos_livros():
    print("\n===== LISTANDO TODOS OS LIVROS ======")
    read_livros()

#===============================================================================================================

EMPRESTIMOS = 'emprestimos.txt'

def write_emprestimos():
    try:
         if not os.path.exists(EMPRESTIMOS):
            with open(EMPRESTIMOS,'w'):
                print("\nCriando arquivo dos livros")
    except Exception as e:
        print(f"Error:{e}")
        print("\nCarregando arquivo dos livros")

def append_emprestimos(codigo_emprestimo,data,vencimento,nome_livro,codigo_livro):
    try:
        with open(EMPRESTIMOS, 'a') as arquivo:
            linha = f'{codigo_emprestimo};{data};{vencimento};{nome_livro};{codigo_livro}'
            arquivo.write(linha)
    except Exception as e:
        print(f"Error:{e}")

def read_emprestimos():
    try:
        with open(EMPRESTIMOS,'r') as arquivo:
            linhas = arquivo.readlines()

            if len(linhas) == 0:
                print("\nLista de emprestimos vazia !")
            else:
                for linha in linhas:
                    dados = linha.strip().split(";")
                    print(f"\nCodigo Emprestimo:{dados[0]}"
                          f"\nData:{dados[1]}"
                          f"\nVencimento do Emprestimo:{dados[2]}"
                          f"\nNome do Livro:{dados[3]}"
                          f"\nCodigo do Livro:{dados[4]}")
                    return dados
    except Exception as e:
        print(f"Error:{e}")

def realizar_emprestimo():
    print("\n===== REALIZANDO EMPRESTIMO =====")
    try:
        write_emprestimos()
        codigo_emprestimo = gerar_codigo_emprestimo()

        data = date.today()
        vencimento = timedelta(days=15)

        nome_livro =  input("Digite o nome do livro: ")
        codigo_livro = input("Digite o codigo do livro: ")
        buscar_livro_pelo_codigo(codigo_livro)

        append_emprestimos(codigo_emprestimo,data,vencimento,nome_livro,codigo_livro)
        print("\nEmprestimo realizado com sucesso !"
              f"\nCodigo Emprestimo:{codigo_emprestimo}"
              f"\nLivro:{nome_livro}")

    except Exception as e:
        print(f"Error:{e}")

def gerar_codigo_emprestimo():
    try:
        with open(EMPRESTIMOS,'r') as arquivo:
            linhas =  arquivo.readlines()
            codigo_emprestimo = 'E00' + str(len(linhas)+1)
            return codigo_emprestimo
    except Exception as e:
        print(f"Error:{e}")


def listar_todos_emprestimos():
    print("\n===== LISTANDO EMPRESTIMOS =====")
    read_emprestimos()

def buscar_emprestimo_pelo_codigo(codigo_emprestimo):
    print("\n===== BUSCANDO EMPRESTIMO PELO CODIGO =====")
    dados = read_emprestimos()
    if dados[0] == codigo_emprestimo:
        return dados
    else:
        print("Nenhum emprestimo encontrado")


