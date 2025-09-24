"""  CIDADE """
cidades = []

def cadastrar_cidade():
    print("\n========== CADASTRANDO CIDADE ==========")
    codigo = "00" + str(gerar_codigo())
    
    nome = input("Digite o nome da cidade: ")
    if validar_nome_cidade(nome):
        return

    estado = input("Digite o nome do estado: ")
    if validar_estado(estado):
        return
    
    cidade = [codigo, nome, estado]
    cidades.append(cidade)
    print("\nCIDADE CADASTRADA COM SUCESSO")
    print(f"Codigo:{cidade[0]} - Cidade: {cidade[1]} - Estado: {cidade[2]}")

def gerar_codigo():
    if len(cidades) == 0:
        codigo = 1
    else:
        codigo = len(cidades)+1
    return codigo

def validar_estado(estado):
    if len(estado) > 2 or len(estado) <= 1:
        print("\nESTADO DEVE TER APENAS 2 LETRAS EX: SP")
        return True
    return False

def validar_nome_cidade(cidade):
    if len(cidade) < 3:
        print("\nNOME DA CIDADE NÃO PODE SER MENOR QUE 3 LETRAS")
        return True
    return False

def buscar_pelo_codigo(codigo):
    print("\n========== BUSCAR POR CODIGO ========")
    if len(cidades) == 0:
        print("\nCADASTRE UMA CIDADE LISTA VAZIA")
    else:
        for cidade in cidades:
            if cidade[0] == codigo:
                print(f"Codigo:{cidade[0]} - Cidade: {cidade[1]} - Estado: {cidade[2]}")


def listar_todas_cidades():
    print("\n========== LISTANDO TODAS CIDADES =========")
    if len(cidades) == 0:
        print("\nCADASTRE UMA CIDADE LISTA VAZIA")
    else:
        for cidade in cidades:
            print(f"Codigo:{cidade[0]} - Cidade: {cidade[1]} - Estado: {cidade[2]}")

'''  ELEITOR '''

eleitores = []

def cadastrar_eleitor():
    print("\n=========== CADASTRANDO ELEITOR =========")
    
    nome = input("Digite o nome do eleitor: ")
    if valida_nome(nome):
        return
    
    titulo = input("Digite o titulo do eleitor: ")
    if valida_titulo(titulo):
        return
    
    cidade = input("Digite a cidade do eleitor: ")
    if validar_nome_cidade(nome):
        return
    
    eleitor = [nome, titulo, cidade]
    eleitores.append(eleitor)
    print(f"\nELEITOR CADASTRADO COM SUCESSO")
    print(f"Nome:{eleitor[0]} - Titulo:{eleitor[1]} - Cidade:{eleitor[2]}")

#VALIDAR NOME
def valida_nome(nome):
    if len(nome) < 4:
        print("NOME NÃO PODE SER MENOR QUE 4 LETRAS")
        return True
    return False

#VALIDAR TITULO
def valida_titulo(titulo):
    if len(titulo) < 13:
        print("ERRO: QUANTIDADE DE NUMERO INVALIDOS")
        return True
    return False

def listar_todos_eleitores():
    print("\n========== LISTANDO TODOS ELEITORES ==========")
    if len(eleitores) == 0:
        print("LISTA DE ELEITORES VAZIA ADICIONE")
    else:
        for eleitor in eleitores:
            print(f"Nome:{eleitor[0]} - Titulo:{eleitor[1]} - Cidade:{eleitor[2]}")

def buscar_pelo_titulo(titulo):
    print("\n========== BUSCAR ELEITOR PELO TITULO ==========")
    if len(eleitores) == 0:
        print("LISTA DE ELEITORES VAZIA ADICIONE")
    else:
        for eleitor in eleitores:
            if eleitor[1] == titulo:
                print(f"Nome:{eleitor[0]} - Titulo:{eleitor[1]} - Cidade:{eleitor[2]}")
            else:
                print("NENHUM ELEITOR ENCONTRADO")
                return
            
def listar_por_cidade(cidade):
    print("\n========== LISTAR ELEITOR POR CIDADE ===========")
    if len(eleitores) == 0:
        print("LISTA DE ELEITORES VAZIA ADICIONE")
    else:
        for eleitor in eleitores:
            if eleitor[2] == cidade:
                print(f"Nome:{eleitor[0]} - Titulo:{eleitor[1]} - Cidade:{eleitor[2]}")
            else:
                print("NENHUM ELEITOR ENCONTRADO")
                return