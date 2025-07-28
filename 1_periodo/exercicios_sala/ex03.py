aluno = []
notas = []
for i in range(1,3):
    print(i, "Aluno")
    nome = input('Digite seu nome:')
    nota = float(input('Digite sua nota:'))
    aluno.append(nome)
    notas.append(nota)

media = sum(notas)/ len(notas)
indice_maior = notas.index(max(notas))
indice_menor = notas.index(min(notas))
maior_nota = max(notas)
menor_nota = min(notas)

acima_media =0
print('Lista de alunos acima da média')
for i in range(len(notas)):
    if notas[i] > media:
        print(f'Aluno:{nome[i]} {nota[i]}')

print('\nListando alunos em ordem alfabetica:')
lista = sorted(nome)
for i in lista:
    print(f'Aluno: {i}')

print(f'A média dos alunos é: {media}')
print(f'Alunos com nota acima da média {acima_media}')
print(f'Aluno com maior nota\n{nome[indice_maior]}\nNota:{maior_nota}')
print(f'Aluno com maior nota\n{nome[indice_menor]}\nNota:{menor_nota}')
