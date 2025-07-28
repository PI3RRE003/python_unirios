windows = []
linux = []
macos = []
outros = []

while True:

    print('\nQual melhor SO para uso institucional:')
    print('1-windows\n2-linux\n3-macos\n4-outros\n0-sair')
    print('Resultado apos digitar 0')

    voto = int(input('Digite seu voto: '))

    if voto == 1:
        windows.append(voto)
    elif voto == 2:
        linux.append(voto)
    elif voto == 3:
        macos.append(voto)
    elif voto == 4:
        resposta = input('Resposta: ')
        outros.append(resposta)
    elif voto == 0:
        print('Resultados:\n')
        print(f'Windows:{sum(windows)}')
        print(f'linux:{sum(linux)}')
        print(f'MacOs:{sum(macos)}')
        print(f'Outros:{outros}')
        print('finalizando o programa.....')
        break
    else:
        print('ERRO')
        break