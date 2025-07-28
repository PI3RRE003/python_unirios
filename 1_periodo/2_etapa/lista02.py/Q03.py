while True:
    print('\nEmprestimo bancario')

    idade = int(input('Digite sua idade:'))
    if idade > 21:
        print(f'\nIDADE VÁLIDA:{idade}\n')
    else:
        print('\nIDADE INVÁLIDA!\n')
        break
    renda = float(input('Digite sua renda:'))
    if renda > 2000:
        print(f'\nRENDA VÁLIDA:{renda}\n')
    else:
        print('\nRENDA INVÁLIDA, RENDA MENSAL MINIMA:2000\n')
        break
    tempo_trabalho = float(input('Tempo de trabalho:'))
    if tempo_trabalho > 1.0:
        print(f'\nTEMPO DE TRABALHO VÁLIDO:{tempo_trabalho}\n')
    else:
        print('\nTEMPO DE TRABALHO INVÁLIDO MINIMO: 1 ANO\n')
        break
        