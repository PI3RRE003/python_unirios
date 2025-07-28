print('Reajuste de salario por cargo')
print('Codigo:\n01 - Vendedor\n02 - Secretario\n03 - Gerente\n04 - Estagiario')
cargo = int(input('Digite seu cargo: '))


if cargo == 1:
    print(f'\nOpção escolhida: Vendedor')
    salario = float(input('Digite seu salario R$: '))
    percentual = 0.5
    aumento = (salario*percentual)
    novo_salario = salario + aumento
    print(f'\nSalario anterior: {salario}\nPercentual: 50%\nAumento:{aumento}\nNovo Salario:{novo_salario}')
elif cargo == 2:
    print(f'\nOpção escolhida: Secretario')
    salario = float(input('Digite seu salario R$: '))
    percentual = 0.35
    aumento = (salario*percentual)
    novo_salario = salario + aumento
    print(f'\nSalario anterior: {salario}\nPercentual: 35%\nAumento:{aumento}\nNovo Salario:{novo_salario}')
elif cargo == 3:
    print(f'\nOpção escolhida: Gerente')
    salario = float(input('Digite seu salario R$: '))
    percentual = 'Sem aumento'
    aumento = 'Sem aumento'
    novo_salario = salario
    print(f'\nSalario anterior: {salario}\nPercentual: {percentual}\nAumento:{aumento}\nNovo Salario:{novo_salario}')
elif cargo == 4:
    print(f'\nOpção escolhida: Estagiario')
    salario = float(input('Digite seu salario R$: '))
    percentual = 0.10
    aumento = (salario*percentual)
    novo_salario = salario + aumento
    print(f'\nSalario anterior: {salario}\nPercentual: 10%\nAumento:{aumento}\nNovo Salario:{novo_salario}')
