import os
while True:
    print('\nCALCULADORA\n')
    print('OPERAÇÃO\n'\
    '===============\n' \
    '1 - SOMA\n' \
    '2 - SUBTRAÇÃO\n' \
    '3 - DIVISÃO\n' \
    '4 - MULTIPLICAÇÃO\n'
    '0 - SAIR\n'
    '===============\n')

    
    try:
        print('BEM VINDO À CALCULADORA')
        operacao = int(input('Digite o código da operação (0 a 4):'))
        if operacao < 0 or operacao > 4:
            print('DIGITE NÚMEROS VÁLIDOS')
    except ValueError:
        print('VOCÊ PRECISA DIGITAR UM NÚMERO INTEIRO')
    except Exception as e:
        print(f'ERRO INESPERADO: {e}')
    
    if operacao == 1:
        print('\nSOMA')
        n1 = float(input('Digite o primeiro numero:'))
        n2 = float(input('Digite o segundo numero:'))
        soma = n1+n2
        print(f'A SOMA DE {n1} + {n2} = {soma}')
    elif operacao == 2:
        print('\nSUBTRAÇÃO')
        n1 = float(input('Digite o primeiro numero:'))
        n2 = int(input('Digite o segundo numero:'))
        subtracao = n1-n2
        print(f'A SUBTRAÇÃO DE {n1} - {n2} = {subtracao}')
    elif operacao == 3:
        print('\nDIVISÃO')
        n1 = float(input('Digite o primeiro numero:'))
        n2 = float(input('Digite o segundo numero:'))
        divisao = n1/n2
        print(f'A DIVISÃO DE {n1} / {n2} = {divisao}')
    elif operacao == 4:
        print('\nMULTIPLICAÇÃO')
        n1 = float(input('Digite o primeiro numero:'))
        n2 = float(input('Digite o segundo numero:'))
        multiplicacao = n1*n2
        print(f'A MULTIPLICAÇÃO DE {n1} * {n2} = {multiplicacao}')
    elif operacao == 0:
        print('ENCERRANDO O PROGRAMA...')
        print('PARA REALIZAR MAIS CALCULOS INICIE NOVAMENTE A CALCULADORA')
        exit()