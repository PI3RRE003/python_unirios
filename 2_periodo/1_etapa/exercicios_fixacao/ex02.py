def listar_maiores_25(dados):
    for chave, valor in dados.items():
        if valor > 25 :
            print(f'Pessoas com Idade Maior que 25:\n\
                    \nNome: {chave}- Idade: {valor}')
        else:
            print('Ninguem acima dos 25')

def media_idades(dados):
    media = sum(dados.values()) / len(dados.values())
    print(f'Média das idades:{media}')

pessoa = {}
for i in range(1,3):
    nome = input('\nDigite seu nome: ')
    idade = int(input('Digite sua idade:'))
    pessoa[nome] = idade
    

listar_maiores_25(pessoa)
media_idades(pessoa)