import json

BIBLIOTECA = 'biblioteca.txt'

def carregar_dados():
    try:
        with open('biblioteca.txt', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Error: lista não existe, começando uma lista vazia")
        return []
    except json.JSONDecodeError:
        print("Error: Arquivo corrompido, iniciando uma lista vazia")
        return []

biblioteca = carregar_dados()

def salvar_dados(biblioteca):
    with open('biblioteca.txt', 'w', encoding='utf-8') as arquivo:
        json.dump(biblioteca, arquivo, indent=4, ensure_ascii=False)


def adicionar_livro():
    print("\n===== ADICIONANDO LIVRO =====")
    try:

        titulo = input("Digite o titulo: ")
        if verifica_existencia_livro(titulo):
            return

        autor = input("Digite o autor: ")
        ano_de_publicacao = input("Digite o ano de publicação: ")

        livro = {
            'titulo' : titulo,
            'autor' : autor,
            'ano' : ano_de_publicacao,
            'status' : status()
        }
        biblioteca.append(livro)
        salvar_dados(biblioteca)
        print(f"\nLivro adicionado com sucesso !!!"
              f"\nTitulo:{livro['titulo']}"
              f"\nAutor:{livro['autor']}"
              f"\nAno de Publicação:{livro['ano']}"
              f"\nStatus:{livro['status']}")
    except Exception as e:
        print(f"Error: {e}")

def status():
    print("\n===== STATUS DO LIVRO ======")
    while True:
        try:
                op = int(input("Digite o status do Livro"
                           "\n1 - Finalizado"
                           "\n2 - Não Finalizado"
                           "\nOpção: "))
                if op == 1:
                    status = 'Finalizado'
                    salvar_dados(biblioteca)
                    return status
                elif op == 2:
                    salvar_dados(biblioteca)
                    status = 'Não Finalizado'
                    return status
        except ValueError:
            print("\nError: Digite 1 ou 2 espaço não pode ser em branco ou ter letras\n")

def verifica_existencia_livro(titulo):
    try:
        for livro in biblioteca:
            if livro['titulo'].lower() == titulo.lower():
                print("Error: Já existe um livro com este titulo")
            else:
                pass
    except Exception as e:
        print(f"Error:{e}")

def listar_livros_lidos():
    print("\n===== LISTANDO LIVROS LIDOS =====")
    try:
        if verifica_lista_livros():
            pass
        else:
            for livro in biblioteca:
                if livro['status'] == 'Finalizado':
                    print(f"\nTitulo:{livro['titulo']}"
                      f"\nAutor:{livro['autor']}"
                      f"\nAno de Publicação:{livro['ano']}")
    except Exception as e:
        print(f"Error:{e}")


def listar_livros_nao_lidos():
    print("\n===== LISTANDO LIVROS NÃO LIDOS =====")
    try:
        if verifica_lista_livros():
            pass
        else:
            for livro in biblioteca:
                if livro['status'] == 'Não Finalizado':
                    print(f"\nTitulo:{livro['titulo']}"
                          f"\nAutor:{livro['autor']}"
                          f"\nAno de Publicação:{livro['ano']}")
    except Exception as e:
        print(f"Error:{e}")

def verifica_lista_livros():
    if len(biblioteca) == 0:
        print("Biblioteca Vazia")
        op = int(input("\nDeseja Adicionar?"
                       "\n1 - Sim"
                       "\n2 - Não"
                       "\nOpção:"))

        if op == 1:
            print("\nRedirecionando para adiconar livro")
            return  adicionar_livro()
        elif op == 2:
            print("\nRetornando ao Menu principal...")
            return
        else:
            print("\nDigite um número válido")
    else:
        pass

def marcar_como_lido():
    print("\n====== MARCANDO LIVRO COMO CONCLUIDO ======")
    try:
        titulo = input("\nDigite o titulo que deseja marcar como lido: ")
        for livro in biblioteca:
            if livro['titulo'].lower() == titulo.lower():
                print(f"\nTitulo:{livro['titulo']}"
                  f"\nAutor:{livro['autor']}"
                  f"\nAno de Publicação:{livro['ano']}"
                  f"\nStatus:{livro['status']}")
                status()
                salvar_dados(biblioteca)
            else:
                print("Livro não encontrado")
    except Exception as e:
        print(f"Error:{e}")

def buscar_livro(termo_busca):
    print("\n===== BUSCANDO LIVRO PELO TERMO =====")
    try:
        for livro in  biblioteca:
            if livro['titulo'].lower() == termo_busca.lower() or livro['autor'].lower() == termo_busca.lower():
                print(f"\nTitulo:{livro['titulo']}"
                      f"\nAutor:{livro['autor']}"
                      f"\nAno de Publicação:{livro['ano']}"
                      f"\nStatus:{livro['status']}")
    except Exception as e:
        print(f"Error:{e}")
