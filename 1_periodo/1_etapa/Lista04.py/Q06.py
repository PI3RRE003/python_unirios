masculino = 0
feminino = 0
idade_media_m = 0
qtd_homens_18_35 = 0
altura_m = 0
altura_f = 0
altura_superior = 0

for i in range(1,3):
    print('Coleta de dados')
    sexo = int(input('0-feminino 1-masculino : '))
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))

    if sexo == 0:
        feminino += 1
        altura_f += altura
    elif sexo == 1:
        masculino += 1
        altura_m += altura

    if sexo == 1 and idade >= 18 and idade <= 35:
        idade_media_m += idade
        qtd_homens_18_35 += 1

    if altura >= 1.80:
        altura_superior += 1

media_altura_mulheres = altura_f/feminino
media_idade_homens =  idade_media_m / qtd_homens_18_35

print(f'Média da altura das mulheres:{media_altura_mulheres}')
print(f'Média da idade dos homens com 18 e 35 anos:{media_idade_homens}')
print(f'Quantidade de pessoas com altura superior a 1.80m:{altura_superior}')
# ERREI A LOGICA DA IDADE MASCULINA