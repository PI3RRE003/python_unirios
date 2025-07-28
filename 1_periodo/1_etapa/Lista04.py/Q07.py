candidato_1 = 0
candidato_2 = 0
branco_nulo = 0

while True:
    print('\nVOTAÇÃO 2026\n01 - CANDIDATO1\n02 - CANDIDATO2\nNulo qualquer numero acima de 2')
    voto = int(input('Digite seu voto:'))

    if voto == 1:
        candidato_1+=1
    elif voto == 2:
        candidato_2+=1
    elif voto == -1:
        print('Encerrando votação...')
        break
    else:
        branco_nulo+=1

print(f'\ncandidato 01:{candidato_1}')
print(f'candidato 02:{candidato_2}')
print(f'Branco/Nulos:{branco_nulo}')