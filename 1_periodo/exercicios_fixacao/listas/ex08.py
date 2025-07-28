aprovado = []
nao_aprovado = []

for i in range(1, 4):
    print('Gostou do produto? (sim ou nao)')
    op = input('Voto: ').strip().lower()

    if op == 'sim':
        aprovado.append(1)
    elif op == 'nao':
        nao_aprovado.append(1)
    else:
        print("Resposta inválida. Digite apenas 'sim' ou 'nao'.")

total = sum(aprovado) + sum(nao_aprovado)

if total > 0:
    percentual = (sum(aprovado) / total) * 100
    print(f'\nNúmero de SIM: {sum(aprovado)}')
    print(f'Número de NÃO: {sum(nao_aprovado)}')
    print(f'Percentual de aprovação: {percentual:.2f}%')
else:
    print("Nenhum voto válido registrado.")

