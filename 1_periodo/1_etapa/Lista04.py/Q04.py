menor_idade =0
media_menor = 0
maior_idade =0
media_maior = 0

for i in range(1,21):
    idade = int(input(f'Digite a {i} idade: '))

    if idade < 18:
        menor_idade +=1
        media_menor += idade
    elif idade > 18:
        maior_idade +=1
        media_maior += idade

calculo_media_maior =  media_maior / maior_idade
calculo_media_menor = media_menor / menor_idade

print(f'Quantidade de pessoas menores de idade:{menor_idade}')
print(f'Média das pessoas menores de idade:{calculo_media_menor:.2f}')
print(f'Quantidade de pessoas maiores de idade:{maior_idade}')
print(f'Média das pessoas maiores de idade:{calculo_media_maior:.2f}')
