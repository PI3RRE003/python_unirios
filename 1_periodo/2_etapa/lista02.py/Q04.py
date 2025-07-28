while True:
    print('Descontos do salário')
    salario_bruto = float(input('Digite seu salário:'))
    
    #CALCULA O INSS
    if salario_bruto <= 5000:
        inss = 0.10
        desconto_inss = inss * salario_bruto
    elif salario_bruto > 5000:
        inss = 0.15
        desconto_inss = inss * salario_bruto
    
    #CALCULA IMPOSTO DE RENDA
    if salario_bruto <= 2500:
        ir = 0
        desconto_ir = ir * salario_bruto
    elif salario_bruto > 2500 and salario_bruto <= 5000:
        ir = 0.05
        desconto_ir = ir * salario_bruto
    elif salario_bruto > 5000:
        ir = 0.10
        desconto_ir = ir * salario_bruto

    salario_liquido = salario_bruto - desconto_inss - desconto_ir

    print(f'\nSalario Bruto:{salario_bruto}\nDesconto INSS:{desconto_inss}\nDesconto Imposto de renda:{desconto_ir}\nSalario liquído:{salario_liquido}\n')