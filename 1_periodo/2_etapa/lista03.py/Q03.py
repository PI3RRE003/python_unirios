filme_1 = 0
filme_2 = 0
filme_3 = 0
voto_em_branco = 0
while True:
    print('\nVOTAÇÃO PARA MELHOR FILME DO CINEMA:')
    print('Ainda Estou Aqui (Código 01)\
         \nDeadpool & Wolverine (Código 02)\
         \nAuto da Compadecida 2 (Código 03)\
         \nVotos Brancos (Código 00)\n')
    voto = int(input('\nDigite seu voto:'))

    if voto < -1 or voto > 3:
        voto_em_branco +=1

    if voto == 1:
        filme_1 +=1
    elif voto == 2:
        filme_2 +=1
    elif voto == 3:
        filme_3 +=1
    elif voto == 0:
        voto_em_branco +=1
    elif voto == -1:
        print(f'\nTotal de votos para cada filme:\
              \nAinda Estou Aqui:{filme_1}\
              \nDeadpool & Wolverine:{filme_2}\
              \nAuto da Compadecida 2:{filme_3}\
              \nVotos Brancos:{voto_em_branco}')
        
        #VENCEDOR
        if filme_1 > filme_2 and filme_1 >  filme_3:
            print(f'\nVENCEDOR:\nAinda Estou Aqui:{filme_1}\n')
        elif filme_2 > filme_1 and filme_2 > filme_3:
            print(f'\nVENCEDOR:\nDeadpool & Wolverine:{filme_2}\n')
        elif filme_3 > filme_1 and filme_3 > filme_2:
            print(f'\nVENCEDOR:\nAuto da Compadecida 2:{filme_3}\n')

        # EMPATE
        if filme_1 == filme_2:
            print(f'\nEMPATE:\n\
                  \nAinda Estou Aqui:{filme_1}\
                  \nDeadpool & Wolverine:{filme_2}')
        elif filme_1 == filme_3:
            print(f'EMPATE:\n\
                  \nAinda Estou Aqui:{filme_1}\
                  \nAuto da Compadecida 2:{filme_3}')
        elif filme_2 == filme_3:
            print(f'EMPATE:\n\
                  \nDeadpool & Wolverine:{filme_2}\
                  \nAuto da Compadecida 2:{filme_3}')
            
        #VOTOS VALIDOS
        votos_validos = (filme_1 + filme_2 + filme_3) 
        print(f'\nVotos válidos:{votos_validos}')

        #VOTOS EM BRANCO
        print(f'Votos nulos/brancos:{voto_em_branco}')
        exit('\n')