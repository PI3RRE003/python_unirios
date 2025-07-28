print('Calcula média')
n1 = int(input('Digite a 1 nota: '))
n2 = int(input('Digite a 2 nota: '))
n3 = int(input('Digite a 3 nota: '))

media =(n1 + n2 +n3)/3

if media >= 10:
    print(f'Aprovado com distinção: {media}')
elif media >= 7 and media < 10:
    print(f'Aprovado: {media}')
elif media < 7:
    print(f'Reprovado: {media}')

