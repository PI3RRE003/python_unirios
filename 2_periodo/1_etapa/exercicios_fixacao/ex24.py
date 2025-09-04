def realizar_enquete(pergunta, opcoes):
    """
    Esta função conduz a enquete.
    Ela exibe a pergunta, coleta e valida os votos, e retorna a contagem.
    """
    print(f'\n========== ENQUETE: {pergunta} ==========')

    # Cria uma lista para contar os votos, com um zero para cada opção.
    votos = [0] * len(opcoes)
    
    # MELHORIA: Exibe as opções apenas uma vez, fora do loop de votação.
    print("--- Opções de Voto ---")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i} - {opcao}")
    print("0 - Encerrar Votação")
    print("----------------------")

    while True:
        try:
            # MELHORIA: Adicionado try-except para o voto
            voto_usuario = int(input('Digite seu voto: '))

            if voto_usuario == 0:
                print("Votação encerrada.")
                break

            if 1 <= voto_usuario <= len(opcoes):
                votos[voto_usuario - 1] += 1
                print("Voto computado com sucesso!")
            else:
                print("ERRO: Opção inválida. Por favor, vote novamente.")

        except ValueError:
            print("ERRO: Por favor, digite apenas números.")
        
    return votos

def exibir_resultados(pergunta, opcoes, votos):
    """Esta função recebe os resultados e os exibe de forma organizada."""
    print(f"\n========== RESULTADO DA ENQUETE: {pergunta} ==========")

    total_votos = sum(votos)

    if total_votos == 0:
        print('Nenhum voto foi registrado.')
        return

    for i, opcao in enumerate(opcoes):
        contagem = votos[i]
        porcentagem = (contagem / total_votos) * 100 if total_votos > 0 else 0
        print(f'- {opcao}: {contagem} voto(s) ({porcentagem:.2f}%)') # Adicionei o '%' para clareza

    print("-----------------------------------------------------")
    print(f"Total de votos: {total_votos}")

def menu():
    """Função principal que gerencia o programa."""
    while True:
        print('\n========== MENU PRINCIPAL ==========')
        print('1 - Iniciar uma nova enquete')
        print('0 - Sair do programa')
        
        op_str = input('Digite a opção: ')

        try:
            # MELHORIA: try-except para a opção do menu
            op = int(op_str)
            
            if op == 1:
                pergunta = input('Digite a pergunta da enquete: ')
                if pergunta == '':
                    print('ERRO: A pergunta não pode estar vazia.')
                    continue

                num_opcoes_str = input('Digite a quantidade de opções: ')
                num_opcoes = int(num_opcoes_str) # Isso também pode gerar ValueError
                
                if num_opcoes <= 0:
                    print('ERRO: A quantidade de opções deve ser maior que zero.')
                    continue
                
                listar_opcoes = []
                for i in range(num_opcoes):
                    texto_opcao = input(f'Digite o texto da opção {i+1}: ')
                    if texto_opcao == '':
                         print("ERRO: O texto da opção não pode ser vazio.")
                         # Simplesmente adiciona um placeholder para não quebrar
                         listar_opcoes.append(f"Opção {i+1} (vazia)")
                    else:
                         listar_opcoes.append(texto_opcao)

                # CORREÇÃO: Passando a LISTA de opções, não a quantidade
                resultado_votos = realizar_enquete(pergunta, listar_opcoes)
                exibir_resultados(pergunta, listar_opcoes, resultado_votos)

            elif op == 0:
                print('Encerrando o programa....')
                break
            else:
                print("ERRO: Opção de menu inválida. Tente novamente.")

        except ValueError:
            print("ERRO: Entrada inválida. Por favor, digite apenas números para as opções.")

# Inicia o programa
menu()