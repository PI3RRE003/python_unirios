while True:
    print('\nCALCULA CONTA TELEFONICA\n')
    ligacao = int(input('LIGAÇÕES INTERURBANAS TELEFONE:\n1 - RESIDENCIAL\n2 - COMERCIAL\nOPÇÃO(1 OU 2):'))
    qtd_minutos = int(input('\nQUANTIDADE DE MINUTOS UTILIZADOS EM LIGAÇÕES INTERURBANAS:'))
    internet = int(input('\nDIGITE A VELOCIDADE UTILIZADA NO PLANO:\n200 MEGA\n500 MEGA\nPLANO:'))
    
    if internet == 200:
        internet = 50
    elif internet == 500:
        internet = 100

    if ligacao == 1:
        residencial = 2
        total_ligacao = residencial * qtd_minutos
        total_ligacao_internet = total_ligacao + internet
    elif ligacao == 2:
        comercial = 4
        total_ligacao = comercial * qtd_minutos
        total_ligacao_internet = total_ligacao + internet

    print(f'\nVALOR TOTAL DE LIGAÇÕES INTERURBANAS R$:{total_ligacao}\nVALOR DO PLANO DE INTERNET R$:{internet}\nVALOR TOTAL DA CONTA A PAGAR R$:{total_ligacao_internet}')