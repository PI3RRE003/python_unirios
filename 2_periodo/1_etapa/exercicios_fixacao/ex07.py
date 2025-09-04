def media_contas(valores):
    media = sum(valores.values())/len(valores)
    print(f'Média das contas: {media}')

def acima_da_media(valores):
    media = sum(valores.values())/len(valores)
    valor = valor_conta_de_luz
    if valor > media:
        print(f'Valores acima da Média:{valor} da residencia de: {nome_residencia}')
def contas_menores_100(valores):
    contas = 0
    contagem = 0
    for contas in valores.values():
        if contas < 100:
            contagem +=1
            print(f'Contas menores que 100: {contagem}')

contas = {}
for i in range(1,2):
    nome_residencia = input('Digite o nome de sua residencia: ')
    valor_conta_de_luz = float(input('Digite o valor da conta de luz: '))
    contas[nome_residencia] = valor_conta_de_luz

#media_contas(contas)    
#acima_da_media(contas)
contas_menores_100(contas)