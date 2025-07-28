aprovados = []
reprovados = []

print('Média Escolar:')
for i in range(1,3):
    nome = input('Digite seu nome: ')
    n1 = float(input('Digite sua 1 nota: '))
    n2 = float(input('Digite sua 2 nota: '))
    n3 = float(input('Digite sua 3 nota: '))

    media = (n1 + n2 + n3)/3

    if media >= 7:
        aprovados.append((nome,media))
    elif media < 7:
        reprovados.append((nome,media))

for aprovado, nota in aprovados:
    print(f'Aprovado:\n{aprovado} - {nota}')
    
for reprovado, nota in reprovados:
    print(f'Reprovado:\n{reprovado} - {nota}')