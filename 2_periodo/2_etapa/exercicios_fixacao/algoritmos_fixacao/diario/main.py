registros = []
REGISTROS = 'diario.txt'

def salvar_dados(registro):
    with open(REGISTROS,'w', encoding='utf-8')as arquivo:
        for registro in registros:
            linha = f'{registro['codigo']};{registro['texto']}\n'
            arquivo.write(linha)


def carregar_dados():
    registros_carregados = []
    try:
        with open(REGISTROS, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:

                linha_limpa = linha.strip()
                if not  linha_limpa:
                    continue

                try:
                    codigo, texto = linha_limpa.split(';', 1)

                    registro = {
                        'codigo': codigo,
                        'texto': texto
                    }
                    registros_carregados.append(registro)

                except ValueError:
                    print("Error: linha mal formatada")
    except FileNotFoundError:
        pass
    return registros_carregados



def adicionar_registro():
    try:
        codigo = "00" + str(gerar_codigo())

        texto = input("Digite o que deseja registrar: ")

        registro = {
            'codigo' : codigo,
            'texto' : texto
        }
        registros.append(registro)
        salvar_dados(registros)

        print(f"\nRegistro adicionado ao diario com sucesso!\nNumero do registro:{registro['codigo']}")
    except Exception as e:
        print(f"Error:{e}")

def gerar_codigo():
    registros = carregar_dados()
    if len(registros) == 0:
        codigo = 1
    else:
        codigo = len(registros)+1
    return  codigo


def ler_diario():
    print("\n===== DIARIO =====")
    try:
        registros = carregar_dados()
        for registro in registros:
            print(f"\nCodigo:{registro['codigo']}\nRegistro:{registro['texto']}")
    except IndexError:
        print("Error: Ocorreu um erro ao listar o registros")




def menu():
    print("\n===== DIARIO PESSOAL =====")
    print("1 - Adicionar registro"
          "\n2 - Ler diario"
          "\n0 - Sair")


def main():
    while True:
        try:
            menu()

            op = int(input("Digite a opção: "))

            if op == 1:
                adicionar_registro()
            elif op == 2:
                ler_diario()
            elif op == 0:
                print("Encerrando o programa.....")
                break
        except ValueError:
            print(f"\nError:Digite apenas numeros de 0 a 2")


main()