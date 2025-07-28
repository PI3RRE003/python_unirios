print('Reajuste de salario Tabajaras')
salario = float(input('Digite seu salario: '))

if salario < 1200:
    aumento = (salario*0.2)
    novo_salario = salario + aumento
    print(f'Salario antes do reajuste:{salario}\nPercentual de aumento:20%\nValor de aumento:{aumento}\nNovo Salario:{novo_salario}')
elif salario >= 1200 and salario < 2500:
    aumento = (salario*0.15)
    novo_salario = salario + aumento
    print(f'Salario antes do reajuste:{salario}\nPercentual de aumento:15%\nValor de aumento:{aumento}\nNovo Salario:{novo_salario}')
elif salario >= 2500 and salario < 3500:
    aumento = (salario*0.10)
    novo_salario = salario + aumento
    print(f'Salario antes do reajuste:{salario}\nPercentual de aumento:10%\nValor de aumento:{aumento}\nNovo Salario:{novo_salario}')
elif salario >= 3500:
    aumento = (salario*0.05)
    novo_salario = salario + aumento
    print(f'Salario antes do reajuste:{salario}\nPercentual de aumento:5%\nValor de aumento:{aumento}\nNovo Salario:{novo_salario}')