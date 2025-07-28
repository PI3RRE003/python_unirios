nomes = []
nota_final = []

for i in range(1, 3):
    nome = input(f'\nDigite o {i}º nome: ')
    nota = float(input(f'Digite a nota final de {nome}: '))
    nomes.append(nome)
    nota_final.append(nota)

aprovados = []
reprovados = []

for i in range(len(nomes)):
    if nota_final[i] >= 7:
        aprovados.append((nomes[i], nota_final[i]))
    else:
        reprovados.append((nomes[i], nota_final[i]))

media = sum(nota_final) / len(nota_final)

print("\n--- Lista de Aprovados ---")
if aprovados:
    for nome, nota in aprovados:
        print(f"{nome} - Nota: {nota}")
else:
    print("Nenhum aprovado.")

print("\n--- Lista de Reprovados ---")
if reprovados:
    for nome, nota in reprovados:
        print(f"{nome} - Nota: {nota}")
else:
    print("Nenhum reprovado.")

print(f"\nMédia da turma: {media:.2f}")
