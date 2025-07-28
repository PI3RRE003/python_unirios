nomes = []
idades =[]

for i in range(1,3):
    nome = input(f'Digite {i} nome: ')
    nomes.append(nome)
    idade = int(input(f'Digite {i} idade: '))
    idades.append(idade)

print('Pessoas com idade maior que 25:')
for j in idades:
    if j > 25:
        indice_nome = idades.index(j)
        print(nomes[indice_nome])
    
media = sum(idades)/len(idades)

print(f'A média das idades é:{media:.2f}')