contador = 0
soma_idade= 0
i = 1
while True:
    idade = int(input(f'Digite {i} idade: '))

    if idade != 0:
        contador += 1
        soma_idade += idade
        i += 1
    else:
        print('Finalizando....')
        break

media = soma_idade / contador
print(f'Media:{media}')