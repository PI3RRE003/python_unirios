while True:
    print('\n--------------------------------------------------\n\
                MENU\n\
           1 – Maior Número\n\
           2 – Menor Número\n\
           3 – Média Aritmética\n\
           0 – Finalizar\n\
--------------------------------------------------\n')
    
    op = int(input('Digite a opção (0 a 3):'))

    if op == 1:
        print('\nMaior número:\n')
        n1 = int(input('Digite o 1 número:'))
        n2 = int(input('Digite o 2 número:'))
        if n1 > n2:
            print(f'\nResultado:{n1} Maior que {n2}\n')
        else:
            print(f'\nResultado:{n2} Maior que {n1}\n')
    elif op == 2:
        print('\nMenor número:\n')
        n1 = int(input('Digite o 1 número:'))
        n2 = int(input('Digite o 2 número:'))
        if n1 < n2:
            print(f'\nResultado:{n1} Menor que {n2}\n')
        else:
            print(f'\nResultado:{n2} Menor que {n1}\n')
    elif op == 3:
        print('\nMédia Aritimetica\n')
        n1 = int(input('Digite o 1 número:'))
        n2 = int(input('Digite o 2 número:'))
        media = (n1 + n2)/2
        print(f'A média aritimetica de {n1} + {n2} e igual à:{media}')
    elif op == 0:
        print('Encerrando o programa...')
        exit()
    else:
        print('Opção invalida')