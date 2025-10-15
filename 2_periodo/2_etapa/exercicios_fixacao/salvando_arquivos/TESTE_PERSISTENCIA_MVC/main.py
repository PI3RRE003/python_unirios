from model.model import *
from view.view import *

def main():
    playlist = carregar_musicas_do_arquivos()
    mostrar_mensagem(f"Bem vindo ! {len(playlist)} musicas carregadas")

    while True:
        opcao = menu()

        if opcao == 1:
            titulo, artista = pedir_dados_nova_musica()

            musica_adicionada = adicionar_musica(playlist, titulo, artista)

            mostrar_mensagem(f"Musica:{musica_adicionada['titulo']} adicionada com sucesso")

        elif opcao == 2:
            mostrar_playlist(playlist)
        elif opcao == 3:
            id_para_remover = pedir_id_para_remover()

            if pedir_id_para_remover() is None:
                sucesso = remover_musica(playlist, id_para_remover)

                if sucesso:
                    mostrar_mensagem("Musica removida com sucesso")
                else:
                    mostrar_mensagem("Erro: Musica com este ID não encontrada")
            else:
                mostrar_mensagem("Error:ID invalido.")

        elif opcao == 0:
            mostrar_mensagem("Ate Logo !!!")
            break
        else:
            mostrar_mensagem("Opção Invalida tente novamente")


if __name__ == '__main__':
    main()
