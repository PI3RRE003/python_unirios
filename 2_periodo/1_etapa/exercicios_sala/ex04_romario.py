aprovados = []
reprovados = []
for i in range(1,6):
    nome = input(f'\n{i} Aluno - nome: ')
    while True:
        n1 = float(input('\nDigite a primeira nota: '))
        if n1 < 0 or n1 > 10:
            continue
        else:
            break
    while True:
        n2 = float(input('\nDigite a segunda nota: '))
        if n2 < 0 or n2 > 10:
            continue
        else:
            break
    
    while True:
        n3 = float(input('\nDigite a terceira nota: '))
        if n3 < 0 or n3 > 10:
            continue
        else:
            break
        
    media = (n1 + n2 + n3) / 3
    
    if media >= 7:
        aprovados.append(nome)
    else:
        reprovados.append(nome)

print(f'Aprovados:{aprovados}')
print(f'Reprovados:{reprovados}')