aplicativos = []
for app in range(1,3):
    print(f'{app} - APP:')
    nome = input('Digite o nome: ')
    tempo_uso = int(input('Digite a quantidade de tempo de uso em horas:'))
    aplicativos.append((nome, tempo_uso))

print('Aplicativos usados por mais de 10h/semana')
for nome, tempo_uso in aplicativos:    
    if tempo_uso > 10:
        aplicativo = f'\nNome:{nome}\nTempo de uso:{tempo_uso}'
        print(aplicativo)

maior_tempo = -1
app_maior = ''
print('\nApliactivo com maior tempo de uso:')
for nome, tempo_uso in aplicativos:
    if tempo_uso > maior_tempo:
        maior_tempo = tempo_uso
        app_maior = nome
        print(f'Nome: {app_maior}\nTempo de uso: {maior_tempo}')