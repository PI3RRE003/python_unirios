aptas = 0
nao_aptas = 0
for pessoas in range(1,5):
    print('REQUISITOS CNH')
    print(f'{pessoas} Pessoa:')
    idade = int(input('Digite sua idade:'))
    alfabetizacao = input('alfabetização (S/N):')
    if idade >= 18 and alfabetizacao == 'S' or alfabetizacao == 's'  :
       print(f'\nATENDE TODOS OS REQUISITOS PARA TIRAR CNH\n') 
       aptas+=1
    elif  idade < 18 and alfabetizacao == 'S' or alfabetizacao == 's':
        print(f'\nNÃO ATENDE OS REQUISITOS MOTIVO:\nIDADE:{idade}\n')
        nao_aptas+=1
    elif idade < 18 and alfabetizacao == 'N' or alfabetizacao == 'n':
        print(f'\nNÃO ATENDE OS REQUISITOS MOTIVO:\nIDADE:{idade}\nALFABETIZAÇÃO:{alfabetizacao}\n')
        nao_aptas+=1
    elif idade >= 18 and alfabetizacao == 'N' or alfabetizacao == 'n':
        print(f'\nNÃO ATENDE OS REQUISITOS MOTIVO:\n\nALFABETIZAÇÃO:{alfabetizacao}\n')

print(f'\nTotal de pessoas aptas:{aptas}\nTotal de pessoas não aptas:{nao_aptas}\n')