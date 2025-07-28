while True:
    print('\nCalcula IMC')
    print('Para encerrar digite "sair" no campo nome\n')
    nome = input('Nome:')
    if nome == 'Sair' or nome == 'SAIR' or nome == 'sair':
        print('\nEncerrando o programa....')
        exit()
    peso = float(input('Peso:'))
    altura = float(input('Altura:'))

    imc = (peso/altura**2)

    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif imc > 18.5 and imc < 24.9:
        classificacao = 'Peso normal'
    elif imc > 25.0 and imc < 29.9:
        classificacao = 'Sobrepeso'
    elif imc > 30:
        classificacao = 'Obesidade'
    
    print(f'\nRESULTADO:\nNome:{nome}\nPeso:{peso}\n{nome}:{classificacao}')