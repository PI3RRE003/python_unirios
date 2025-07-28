numeros_reais = []

for i in range(1,5):

    numeros = float(input('Digite um número: '))
    numeros_reais.append(numeros)

media = sum(numeros_reais) / len(numeros_reais)

acima_media = []

if numeros > media:
    acima_media.append(numeros)

else:
    print('nenhum numero acima da média')

print(f'Média de numeros: {media}')
print(f'Numeros acima da média: {acima_media}')