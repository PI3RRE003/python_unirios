windows = []
linux = []
macOS = []
outro = []

print('============================================')
print('Qual o melhor sistema operacional para uso institucional?')

while True:
    print('\n1 - Windows')
    print('2 - Linux')
    print('3 - Mac OS')
    print('4 - Outro')
    print('0 - Encerrar')

    escolha = input('Digite de "1" a "4" e "0" para encerrar: ')

    if escolha == '1':
        windows.append('Windows')
    elif escolha == '2':
        linux.append('Linux')
    elif escolha == '3':
        macOS.append('Mac OS')
    elif escolha == '4':
        resposta = input('Digite aqui outro sistema: ')
        outro.append(resposta)
    elif escolha == '0':
        print('Encerrando o programa....')
        break
    else:
        print('Digite um número válido.')

print('\nVotos para Windows:')
if len(windows) == 0:
    print('Sem nenhum registro')
else:
    print(len(windows))

print('\nVotos para Linux:')
if len(linux) == 0:
    print('Sem nenhum registro')
else:
    print(len(linux))

print('\nVotos para Mac OS:')
if len(macOS) == 0:
    print('Sem nenhum registro')
else:
    print(len(macOS))

print('\nVotos para outra ISO:')
if len(outro) == 0:
    print('Sem nenhum registro')
else:
    print(len(outro))
    print('Sistemas Informados:')
    for sistema in outro:
        print(f' - {sistema}')

