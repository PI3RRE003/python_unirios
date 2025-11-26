from models import *
def gerenciar_postagens():
    print("\n====== GERENCIANDO POSTAGENS =====")
    print("1 - Publicar Post"
          "\n2 - Listar Posts"
          "\n3 - Ler post detalhado"
          "\n0 - Sair")

def gerenciar_comentarios():
    print("\n===== GERENCIANDO COMENTARIOS =====")
    print("1 - Comentar"
          "\n2 - Ver Comentarios"
          "\n0 - Sair")


def menu():
    while True:
        print("\n===== SISTEMAS DE COMENTARIOS DO BLOG =====")
        print("1 - Gerenciar Postagens"
              "\n2 - Gerenciar Comentarios"
              "\n0 - Sair")

        try:
            op = int(input("Digite a opção: "))
            if op == 1:
                while True:
                    gerenciar_postagens()

                    op1 = int(input("Digite a opção:"))
                    if op1 == 1:
                        publicar_post()
                    elif op1 == 2:
                        listar_posts()
                    elif op1 == 3:
                        post_id = input("Digite o ID do post: ")
                        ler_post_detalhado(post_id)
                    elif op1 == 0:
                        print("Encerrando o programa...")
                        break
            elif op == 2:
                while True:
                    gerenciar_comentarios()

                    op2 = int(input("Digite a opção: "))
                    if op2 == 1:
                        post_id = input("Digite o ID do post: ")
                        comentar(post_id)
                    elif op2 == 2:
                        post_id = input("Digite o ID do post: ")
                        ver_comentarios(post_id)
                    elif op2 == 0:
                        print("\nEncerrando o programa...")
                        break
            elif op == 0:
                print("\nEncerrando o programa...")
                break
        except Exception as e:
            print(f"{e}")

menu()