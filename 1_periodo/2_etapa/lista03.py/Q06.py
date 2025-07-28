maior_indice_acidente = 0
maior_cidade = 0
menor_indice_acidente = 0
menor_cidade = 0

for contador in range(1,21):
    codigo_cidade = int(input(f'\nDigite o codigo da {contador} cidade:'))
    veiculo_passeio = int(input(f'Digite a quantidade de veiculos de passeio da {contador} cidade:'))
    acidentes_com_vitima = int(input(f'número de acidentes de trânsito com vítimas da {contador} cidade:'))

    #GPT
    soma_acidentes_com_vitima += acidentes_com_vitima
    soma_veiculo_passeio += veiculo_passeio
    #GPT
    if acidentes_com_vitima > maior_indice_acidente:
        maior_indice_acidente = acidentes_com_vitima
        maior_cidade = codigo_cidade
    #GPT
    if acidentes_com_vitima < menor_indice_acidente:
        menor_indice_acidente = acidentes_com_vitima
        menor_indice_acidente = codigo_cidade
        
    #GPT
    media_acidente_com_vitima = soma_acidentes_com_vitima / 20
    media_veiculo_passeio = soma_veiculo_passeio / 20

print(f'\nMAIOR INDICE DE ACIDENTE DE TRANSITO:{maior_indice_acidente}')
print(f'CODIGO DA CIDADE COM MAIOR INDICE:{maior_cidade}')
print(f'\nMENOR INDICE DE ACIDENTE DE TRANSITO:{menor_indice_acidente}')
print(f'CODIGO DA CIDADE COM MENOR INDICE:{menor_cidade}')
print(f'\nMÉDIA DE ACIDENTE DE TRANSITO COM VITIMA:{media_acidente_com_vitima}')
print(f'MÉDIA DE VEICULOS DE PASSEIO:{media_veiculo_passeio}')

#MINHA LOGICA DO INICIO SEGUIA CERTO, DOIS IF'S SEPARADOS PARA MAIOR E MENOR INDICE E NÃO PENSEI EM ITERADORES PARA A MÉDIA DE CADA UM