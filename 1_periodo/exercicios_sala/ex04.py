codigos = []
habitantes = []
nascimentos = []
taxas = []

for i in range(1,3):
    print('Cidade', i)
    codigo = input('Informe o codigo: ')
    num_habitantes = int(input('Informe o n° habitantes: '))
    num_nasci = int(input('Informe o n° de nascidos: '))

    codigos.append(codigo)
    habitantes.append(num_habitantes)
    nascimentos.append(num_nasci)

    taxa = (num_nasci*1000)/num_habitantes
    taxas.append(taxa)

indice_maior = taxas.index(max(taxas))
indice_menor = taxas.index(min(taxas))

print(f'Maior Taxa: {taxas[indice_maior]} - cidade {codigos[indice_maior]}')
print(f'Menor Taxa: {taxas[indice_menor]} - cidade {codigos[indice_menor]}')

media_nasci = sum(nascimentos)/len(nascimentos)

print(f'A média de nascimentos nas 5 cidades é: {media_nasci:.1f}')

nasc_pequenas = []
for i in range(5):
    if habitantes[i] < 1000:
        nasc_pequenas.append(nascimentos[i])

media_pequenas = sum(nasc_pequenas)/len(nasc_pequenas)