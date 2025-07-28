print('Eleições 2026')

print('======================')
print('1° - Candidato')
print('2° - Candidato')
print('3° - Candidato')
print('4° - Candidato')
print('5° - Voto Nulo')
print('6° - Voto em branco')
print('0° - Finalizar')
print('======================')

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
nulo = 0
emBranco = 0
total_nulo = 0
total_branco = 0

while True:
    voto = int(input('Digite seu voto:'))

    if voto == 5:
        nulo += 1
        total_nulo = nulo
    elif voto >= 6:
        emBranco +=1
        total_branco = emBranco
    if voto == 1:
        candidato_1 +=1
    elif voto == 2:
        candidato_2 +=1
    elif voto == 3:
        candidato_3 +=1
    elif voto == 4:
        candidato_4 += 1
    elif voto == 0:
        print(f'Vencedor: {mensagem}')
        print(f'Total de votos nulo: {total_nulo}')
        print(f'Total de votos em branco: {total_branco}')
        print('Encerrando o sistema...')
        exit()

    if candidato_1 > candidato_2 and candidato_1 > candidato_3:
        mensagem = f'1° Candidato vencedor com {candidato_1} votos'
    elif candidato_2 > candidato_1 and candidato_2 > candidato_3:
        mensagem = f'2° Candidato vencedor com {candidato_2} votos'
    elif candidato_3 > candidato_1 and candidato_3 > candidato_2:
        mensagem = f'3° Candidato vencedor com {candidato_3} votos'
    elif candidato_1 == candidato_2 and candidato_1 > candidato_3:
        mensagem = f'1° Candidato e 2° candidato empate com {candidato_1} votos'
    elif candidato_1 == candidato_3 and candidato_1 > candidato_2:
        mensagem = f'1° Candidato e 3° candidato empate com {candidato_1} votos'
    elif candidato_2 == candidato_3 and candidato_2 > candidato_1:
        mensagem = f'Empate entre 2° e 3° candidatos com {candidato_2} votos'

    

