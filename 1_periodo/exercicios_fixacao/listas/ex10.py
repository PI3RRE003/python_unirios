nomes = []
notas = []

for i in range(1,6):

    nome = input('Digite seu nome: ')
    nomes.append(nome)

    nota = float(input(f'{nome} digite sua nota 1 a 10: '))
    notas.append(nota)

maior_nota = max(notas)
menor_nota = min(notas)

indice_maior = nomes[notas.index(max(notas))]
indice_menor = nomes[notas.index(min(notas))]

media = sum(notas)/len(notas)

acima_nome = []
acima_sete = []

for i in range(len(notas)):
    if notas[i] > 7:
        acima_nome.append(nomes[i])
        acima_sete.append(notas[i])

print(f'\nAluno com maior nota:{indice_maior}\nNota:{maior_nota}')
print(f'Aluno com menor nota:{indice_menor}\nNota:{menor_nota}')

if acima_nome:
    for i in range(len(acima_nome)):
        print(f'\nAlunos com nota maior que "7" :{acima_nome[i]}, Nota:{acima_sete[i]}')

else:
    print('Nenhum aluno com nota maior que sete')