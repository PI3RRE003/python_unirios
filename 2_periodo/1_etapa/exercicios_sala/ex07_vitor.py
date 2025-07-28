nomes = []
conta_luz = []
for i in range(1,5):
    print(f'\n{i} Pessoa')
    nome = input('Digites seu nome:')
    nomes.append(nome)
    conta = float(input('Digite a conta de luz:'))
    conta_luz.append(conta)

media_contas = sum(conta_luz)/len(conta_luz)

for conta in conta_luz:
    if conta > media_contas:
        acima_media = conta

conta_inferior = []
for conta in conta_luz:
    if conta < 100:
        conta_menor_100 = conta
        conta_inferior.append(conta_menor_100)

print(f'\nValor médio das contas: {media_contas}')
print(f'Valores acima da média: {acima_media}')
print(f'Valores inferiores a R$100: {conta_inferior}')