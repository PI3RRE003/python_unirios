def mostrar_lista(dados):
    for chave, valor in dados.items():
        print(f'{chave} - {valor} ')

def numeros_maiores_50(dados):
    for chave, valor in dados.items():
        if valor >= 50:
            print(f'{chave},{valor}')

def conta_menores_10(dados):
    numero = 0
    for chave, valor in dados.items():
        if valor < 10:
            numero+= 1
            print(f'\n{chave} - {valor}')
    print(f'\nQuantidade de numeros menores que 10: {numero}')

numeros = {}
for i in range(1,4):
    n = int(input(f'Digite {i} número: '))
    numeros[f'num{i}'] = n

mostrar_lista(numeros)
numeros_maiores_50(numeros)
conta_menores_10(numeros)   