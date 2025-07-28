nomes = []
idades = []

for i in range(1,6):

    nome = input(f'\nDigite {i} nome: ')
    nomes.append(nome)

    idade = int(input(f'Digite {i} idade: '))
    idades.append(idade)

mais_velha = max(idades)
indice_1 = nomes[idades.index(max(idades))]

mais_nova = min(idades)
indice_2 = nomes[idades.index(min(idades))]

media_idade = sum(idades) / len(idades)

print(f'\nPessoa mais velha:{indice_1}\nidade: {mais_velha}')
print(f'Pessoa mais nova:{indice_2}\nidade: {mais_nova}')
print(f'Média da idade: {media_idade}')