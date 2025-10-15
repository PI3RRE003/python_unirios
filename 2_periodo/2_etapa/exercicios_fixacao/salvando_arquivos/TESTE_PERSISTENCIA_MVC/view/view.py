def menu():
    print("======== PLAYLIST ========")
    print("1 - Adicionar Musica"
          "\n2 - Listar todas as musicas"
          "\n3 - Remover Musica"
          "\n0 - Sair")

    try:
        return int(input('Escolha uma opção:'))
    except ValueError:
        return  -1


def pedir_dados_nova_musica():
    titulo = input("Digite o titulo: ")
    artista = input("Digite o artista: ")
    return  titulo, artista

def mostrar_playlist(playlist):
    print("\n========= SUA PLAYLIST ========")
    if not playlist:
        print("playlist vazia")
    else:
        for musica in playlist:
            print(f"ID:{musica['id']} - Titulo:{musica['titulo']} - Artista:{musica['artista']}")

def pedir_id_para_remover():
    try:
        return int(input("Digite o ID da musica para remover: "))
    except ValueError:
        return None

def mostrar_mensagem(mensagem):
    print(mensagem)