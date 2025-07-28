for i in range(1, 21):
    print('Desconto INSS')
    salario = float(input(f'Digite {i} salario: '))

    if salario <= 600:
        print(f'Salario:{salario}\nDesconto:Isento')
    elif salario > 600 and salario <= 1200:
        desconto = 0.2
        novo_salario = salario - (salario*desconto)
        print(f'Salario:{salario}\nDesconto:20%\nNovo Salario:{novo_salario}')
    elif salario > 1200 and salario <= 2000:
        desconto = 0.25
        novo_salario = salario - (salario*desconto)
        print(f'Salario:{salario}\nDesconto:25%\nNovo Salario:{novo_salario}')
    elif salario > 2000:
        desconto = 0.3
        novo_salario = salario - (salario*desconto)
        print(f'Salario:{salario}\nDesconto:30%\nNovo Salario:{novo_salario}')