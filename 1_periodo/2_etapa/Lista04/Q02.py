media_mes_temperatura = []
meses= ['Janeiro','fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']


for mes in meses: 
    temperatura = float(input(f'Digite a temperatura em °C mensal {mes} de sua cidade: '))
    media_mes_temperatura.append(temperatura)

media_anual = sum(media_mes_temperatura)/len(media_mes_temperatura)
print(f'\nA media anual da sua cidade é: {media_anual:.2f}°C')
print('Meses acima da média:') 
for i in range(len(meses)):
    if media_mes_temperatura[i] > media_anual:
        print(f'{meses[i]}: {media_mes_temperatura[i]:.2f}°C')

