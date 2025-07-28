windows = []
linux = []
macos = []
outros = []
while True:
    print('==========================================================\
          \nQual o melhor sistema operacional para uso institucional?\
          \n1 - Windows\
          \n2 - Linux\
          \n3 - Mac OS\
          \n4 - Outro\
          \n0 - Sair\
          \n==========================================================')
    
    resposta = int(input('Resposta:'))

    if resposta -1 and resposta > 4:
        print('Digite um número válido de 0 a 4')
        break

    if resposta == 1:
        windows.append(resposta)
    elif resposta == 2:
        linux.append(resposta)
    elif resposta == 3:
        macos.append(resposta)
    elif resposta == 4:
        outro = input('Outro:')
        outros.append(outro)
        for SO in outros:
             outro = outros
    elif resposta == 0:
        print(f'\nVotos para Windows:{sum(windows)}')
        print(f'Votos para Linux:{sum(linux)}')
        print(f'Votos para Mac OS: {sum(macos)}')
        print(f'Votos para Outro: {outro}')
        print('\nENCERRANDO o programa....')
        break

