import os

POST = 'post.txt'
COMENTARIOS = 'comentarios.txt'

def write_posts():
    if not os.path.exists(POST):
        with open(POST,'w'):
            ...

def append_post(id, titulo, autor, texto):
    with open(POST,'a') as arquivo:
        linha = f'{id};{titulo};{autor};{texto}\n'
        arquivo.write(linha)

def read_posts():
    with open(POST, 'r') as arquivo:
        linhas = arquivo.readlines()

        if len(linhas) == 0:
            print("Lista de posts vazia")
        else:
            for linha in linhas:
                dados = linha.strip().split(";")
                print(f"ID: {dados[0]}"
                      f"\nTitulo: {dados[1]}"
                      f"\nAutor: {dados[2]}"
                      f"\nTexto: {dados[3]}")

def publicar_post():
    print("\n====== PUBLICANDO POST =====")
    write_posts()

    id = gerar_id()
    titulo = input("Digite o titulo do post: ")
    autor = input("Digite o autor do post: ")
    texto =  input("Digite o texto do post: ")

    append_post(id,titulo,autor,texto)
    print("\nPost adicionado com sucesso !!!"
          f"\nID:{id}"
          f"\nTitulo:{titulo}"
          f"\nAutor:{autor}"
          f"\nTexto:{texto}")

def gerar_id():
    with open(POST, 'r') as arquivo:
        linhas = arquivo.readlines()
        id = "00" + str(len(linhas)+1)
        return id

def listar_posts():
    print("\n====== LISTANDO POSTS =====")
    read_posts()

def ler_post_detalhado(post_id):
    print("\n====== LENDO POST DETALHADO =====")
    with open(POST,'r') as arquivo:
        linhas = arquivo.readlines()

        if len(linhas) == 0:
            print("Lista de posts vazia")
        else:
            for linha in linhas:
                dados = linha.strip().split(";")
                if dados[0] == post_id:
                    print(f"ID: {dados[0]}"
                          f"\nTexto: {dados[3]}")
                else:
                    print("Post não encontrado")


COMENTARIOS = 'comentarios.txt'

def write_comentarios():
    if not os.path.exists(COMENTARIOS):
        with open(COMENTARIOS,'w'):
            ...

def append_comentario(id_post, nome, comentario):
    with open(COMENTARIOS, 'a') as arquivo:
        linha = f'{id_post};{nome};{comentario};\n'
        arquivo.write(linha)

def comentar(id_post):
    print("\n====== COMENTANDO NO POST =====")
    nome_usuario = input("Digite seu nome para fazer o comentario: ")
    comentario = input("Digite o comentario: ")

    append_comentario(id_post, nome_usuario,comentario)
    print("\nComentario adicionado com sucesso!!!"
          f"\nID Post:{id_post}"
          f"\nUsuario:{nome_usuario}"
          f"\nComentario:{comentario}")

def ver_comentarios(post_id):
    ler_post_detalhado(post_id)
    mostrar_comentarios(post_id)

def mostrar_comentarios(post_id):
    with open(COMENTARIOS,'r') as arquivo:
        linhas = arquivo.readlines()

        if len(linhas) == 0:
            print("Lista de comentarios deste post vazia")
        else:
            for linha in linhas:
                dados = linha.strip().split(";")
                if dados[0] == post_id:
                    print(f'\nUsuario:{dados[1]}'
                          f'\nComentario:{dados[2]}')
                else:
                    print("Comentario não encontrado")