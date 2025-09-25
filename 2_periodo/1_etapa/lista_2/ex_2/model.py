empresas = []

def cadastrar_empresa():
    print("\n========== CADASTRANDO EMPRESA =========")

    nome_empresa = input("Digite o nome da empresa: ")
    if validar_empresa(nome_empresa):
        return
    
    cnpj = input("Digite o CNPJ da empresa: ")
    if validar_cnpj(cnpj):
        return
        
    mercado_de_atuacao = input("Digite o mercado empresa: ")
    if validar_mercado(mercado_de_atuacao):
        return

    numeros_de_funcionarios = input("Digite a quantidade de funcionarios da empresa: ")
    if validar_funcionarios(numeros_de_funcionarios):
        return
    
    empresa = [nome_empresa, cnpj, mercado_de_atuacao, numeros_de_funcionarios]
    empresas.append(empresa)
    print("\nEMPRESA CADASTRADA COM SUCESSO")
    print(f"\nEmpresa:{empresa[0]} - CNPJ:{empresa[1]} - Mercado de atuação:{empresa[2]} - Numero de funcionarios:{empresa[3]}")

def validar_empresa(nome):
    if len(nome) < 4:
        print("\nERRO: NOME DA EMPRESA DEVE CONTER MAIS DE 4 CARACTERES")
        return True
    return False

def validar_cnpj(cnpj):
    if len(cnpj) < 14 or len(cnpj) > 14:
        print("ERRO: TAMANHO DO CNPJ INVÁLIDO")
        return True
    return False

def validar_mercado(mercado):
    if len(mercado) < 4:
        print("ERRO: DIGITE O MERCADO DE ATUAÇÃO")
        return True
    return False

def validar_funcionarios(funcionarios):
    if len(funcionarios) < 1:
        print("ERRO; EMPRESA DEVE CONTER PELO MENOS 1 FUNCIONARIO")
        return True
    return False

def listar_todas_empresas():
    print("========= LISTANDO EMPRESAS =========")
    if len(empresas) == 0:
        print("LISTA DE EMPRESAS VAZIA")
    else:
        for empresa in empresas:
            print(f"Empresa:{empresa[0]} - CNPJ:{empresa[1]} - Mercado de atuação:{empresa[2]} - Numero de funcionarios:{empresa[3]}")

def buscar_empresa_pelo_cnpj(cnpj):
    print("=========== BUSCANDO PELO CNPJ ==========")
    if len(empresas) == 0:
        print("LISTA DE EMPRESAS VAZIA")
    else:
        for empresa in empresas:
            if empresa[1] == cnpj:
                print(f"Empresa:{empresa[0]} - CNPJ:{empresa[1]} - Mercado de atuação:{empresa[2]} - Numero de funcionarios:{empresa[3]}")

def alterar_dados_da_empresa(cnpj):
    print("========= ALTERANDO EMPRESA ==========")
    if len(empresas) == 0:
        print("LISTA DE EMPRESAS VAZIA")
    else:
        for empresa in empresas:
            print(f"Empresa:{empresa[0]} - CNPJ:{empresa[1]} - Mercado de atuação:{empresa[2]} - Numero de funcionarios:{empresa[3]}")

        for empresa in empresas:
            if empresa[1] == cnpj:
                
                nome_empresa = input("Digite o novo nome da empresa: ")
                if validar_empresa(nome_empresa):
                    return
                empresa[0] = nome_empresa

                mercado_de_atuacao = input("Digite o novo mercado da empresa: ")
                if validar_mercado(mercado_de_atuacao):
                    return
                empresa[2] = mercado_de_atuacao

                numeros_de_funcionarios = input("Digite a quantidade atualizada de funcionarios da empresa: ")
                if validar_funcionarios(numeros_de_funcionarios):
                    return
                empresa[3] = numeros_de_funcionarios
                
                print("EMPRESA ATUALIZADA COM SUCESSO")
                print(f"\nEmpresa:{empresa[0]} - CNPJ:{empresa[1]} - Mercado de atuação:{empresa[2]} - Numero de funcionarios:{empresa[3]}")


def deletar_empresa(cnpj):
    for empresa in empresas:
        if empresa[1] == cnpj:
            empresas.remove(empresa)