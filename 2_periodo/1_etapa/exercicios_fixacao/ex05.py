def app_acima_10h(horas):
    for nome, hora in horas.items():
        if hora > 10:
            print(f'App usado mais de 10/h por semana: {nome} - Horas usadas: {hora}')
def app_mais_usado(horas):
    maior_tempo = 0
    for nome, hora in horas.items():
        if hora > maior_tempo:
            maior_tempo = hora
    print(f'\nApp com maior tempo de uso: {nome} - Tempo:{maior_tempo}')

app = {}
for i in range(1,3):
    nome = input('Digite o nome do app: ')
    horas = float(input('Digite horas por semana: '))
    app[nome] = horas

app_acima_10h(app)
app_mais_usado(app)