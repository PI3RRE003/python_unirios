nomes = []
salarios = []

for i in range(1, 5):  # Troque 5 por outro valor se quiser mais pessoas
    nome = input(f'\nDigite o {i}º nome: ')
    nomes.append(nome)

    salario = float(input(f'Digite o salário de {nome}: '))
    salarios.append(salario)

maior_sal = max(salarios)
menor_sal = min(salarios)

indice_maior = nomes[salarios.index(maior_sal)]
indice_menor = nomes[salarios.index(menor_sal)]

media = sum(salarios) / len(salarios)

acima_media_nomes = []
acima_media_salarios = []

for i in range(len(salarios)):
    if salarios[i] > media:
        acima_media_nomes.append(nomes[i])
        acima_media_salarios.append(salarios[i])

print(f'\nMaior salário: {indice_maior} - R$ {maior_sal:.2f}')
print(f'Menor salário: {indice_menor} - R$ {menor_sal:.2f}')
print(f'Média dos salários: R$ {media:.2f}')

print('\n--- Salários acima da média ---')
if acima_media_nomes:
    for i in range(len(acima_media_nomes)):
        print(f'{acima_media_nomes[i]} - R$ {acima_media_salarios[i]:.2f}')
else:
    print('Nenhum salário acima da média.')
