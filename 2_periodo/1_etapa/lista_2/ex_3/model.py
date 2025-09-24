pacientes = []

def registrar_paciente():
    print("\n========== REGISTRANDO PACIENTE ==========")
    nome = input("Digite o nome do paciente: ")
    cpf = input("Digite o CPF do paciente: ")
    telefone = input("Digite o telefone do paciente: ")
    
    paciente = [nome,cpf,telefone]
    pacientes.append(paciente)
    print("\nPACIENTE REGISTRADO COM SUCESSO")
    print(f"Nome:{paciente[0]} - CPF:{paciente[1]} - Telefone:{paciente[2]}")

def validar_cpf(cpf):
    if len(cpf) < 11 or len(cpf) > 11:
        print("ERRO: tamanho do cpf invalido")
        return True
    return False

def verifica_lista_paciente():
    if len(pacientes) == 0:
        print("\nERRO: lista de pacientes vazia")
        
        op = input("Deseja cadastrar? (S/N): ")
        if op == 'S' or op == 's':
            return registrar_paciente()
        elif op == 'N' or op == 'n':
            print("\nRETONANDO AO MENU")
            return True
            

def listar_todos_pacientes():
    if verifica_lista_paciente():
        return 
    
    print("\n========== LISTANDO TODOS OS PACIENTES ===========")
    for paciente in pacientes:
        print(f"Nome:{paciente[0]} - CPF:{paciente[1]} - Telefone:{paciente[2]}")

def alterar_paciente(cpf):
    if verifica_lista_paciente():
        return
    
    print("\n=========== ALTERANDO DADOS DO PACIENTE ==========")
    for paciente in pacientes:
        if paciente[2] == cpf:
            nome = input("Digite o nome completo do paciente: ")
            paciente[1] = nome

            telefone = input("Digite o numero do paciente atualizado: ")
            paciente[2] = telefone

vacinas = []
tipo_vacinas = ['COVID', 'Gripe', 'Sarampo', 'Tétano']

def registrar_vacina():
    codigo = "00" + str(gerar_codigo())
    
    tipo_vacina = input("Tipo de Vacina (COVID, Gripe, Sarampo, Tétano): ")
    if valida_vacinas(tipo_vacina):
        return
    
    nome = input("Digite o nome do paciente: ")
    
    cpf =input("Digite o CPF do paciente: ")
    if validar_cpf(cpf):
        return

    vacina = [codigo, tipo_vacina, nome, cpf]
    vacinas.append(vacina)
    print(f"VACINA REGISTRADA COM SUCESSO")
    print(f"Codigo:{vacina[0]} - Vacina:{vacina[1]} - Paciente: {vacina[2]} - CPF: {vacina[3]}")

def gerar_codigo():
    if len(vacinas) == 0:
        codigo = 1
    else:
        codigo = len(vacinas)+1
    return codigo 

def valida_vacinas(tipo_vacina):
    for vacina in tipo_vacinas:
        if vacina != tipo_vacina:
            print(f"ERRO: vacinas devem ser {', '.join(vacina for vacina in tipo_vacinas)}")
            return True
        return False

def verifica_lista_vacina():
    if len(vacinas) == 0:
        print("\nERRO: lista de vacinas vazia")
        
        op = input("Deseja cadastrar? (S/N): ")
        if op == 'S' or op == 's':
            return registrar_paciente()
        elif op == 'N' or op == 'n':
            print("\nRETONANDO AO MENU")
            return True


def listar_vacina_pelo_cpf(cpf):
    if verifica_lista_vacina():
        return
    
    for vacina in vacinas:
        if vacina[3] == cpf:
            print(f"Paciente: {vacina[2]} - CPF: {vacina[3]} - Vacina:{vacina[1]}")
        
def vacinas_pelo_codigo(codigo):
    if verifica_lista_vacina():
        return

    for vacina in vacinas:
        if vacina[0] == codigo:
            print(f"Codigo:{vacina[0]} - Paciente: {vacina[2]} - CPF: {vacina[3]} - Vacina:{vacina[1]}")

def listar_todas_vacinas():
    if verifica_lista_vacina():
        return

    for vacina in vacinas:
        print(f"Codigo:{vacina[0]} - Vacina:{vacina[1]} - Paciente: {vacina[2]} - CPF: {vacina[3]}")

