nomes = []

for i in range(1,3):
    nome = input('Digite seu nome: ')
    nomes.append(nome)

print('Pesquise seu nome:')
pesquisa = input('Digite seu nome: ')
for i in range(len(nomes)):
    if nomes[i] == pesquisa:
        print(f'Seu nome está na lista: {pesquisa}')
    else:
        print('Seu nome não está na lista')
        break