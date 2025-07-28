meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
temperaturas =[]

for i in range(1,13):

    temperatura = float(input(f'Digite a temperatura do mes {i}: '))
    temperaturas.append(temperatura)

media_anual = sum(temperaturas)/ len(temperaturas)

acima_media = []

for i in range(len(temperaturas)):
    if temperaturas[i] > media_anual:
        acima_media.append(meses[i])
        acima_media.append(temperaturas[i])

print(f'Media anual: {media_anual}')
print(f'Meses acima da media:')
if acima_media:
    for i in range(len(acima_media)):
        print(f'{acima_media[i]}')
else:
    print('Nnehum mes acima da media')