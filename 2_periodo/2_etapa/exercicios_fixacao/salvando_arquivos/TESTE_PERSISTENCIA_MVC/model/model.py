import  json

DB_PLAYLIST = "playlist.json"
playlist = []

def carregar_musicas_do_arquivos():
    try:
        with open(DB_PLAYLIST, 'r', encoding='utf-8') as arquivo:
            return  json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_musicas_no_arquivo(playlist):
    with open(DB_PLAYLIST, 'w', encoding='utf-8') as arquivo:
        json.dump(playlist, arquivo, indent=4)

def adicionar_musica(playlist, titulo, artista):
    novo_id = 1

    if playlist:
        novo_id = playlist[-1]['id'] + 1

    nova_musica = {
        'id': id,
        'titulo' : titulo,
        'artista' : artista
    }

    playlist.append(nova_musica)
    salvar_musicas_no_arquivo(playlist)
    return  nova_musica

def remover_musica(playlist, id_musica):
    musica_para_remover = None
    for musica in playlist:
        if musica['id'] == id_musica:
            musica_para_remover = musica
            break

    if musica_para_remover:
        playlist.remove(musica_para_remover)
        salvar_musicas_no_arquivo(playlist)
        return True
    return False


