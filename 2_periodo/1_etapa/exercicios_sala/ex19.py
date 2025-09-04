def bonus_auxilio_inss(salario):
    if salario <= 500:
        bonus = '5% do salário'
        percent = 0.05
    elif salario > 500 and salario <= 1200:
        bonus = '12% do salário'
        percent = 0.12
    elif salario > 1200:
        bonus = 'Sem bonificação'
        percent = 0

    if salario <= 600:
        auxilio_escola = 150
    elif salario > 600:
        auxilio_escola = 100

    if salario <= 1000:
         desconto_inss = 0
    elif salario <= 2000:
        desconto_inss = 0.08
    elif salario > 2000:
        desconto_inss = 0.10

    novo_salario = salario + (salario*percent) + auxilio_escola - (salario*desconto_inss)
    return f'\nCalculo Finalizado:\nSalario Atual:{salario}\nBonus:{bonus}\nAuxilio Escola:{auxilio_escola}\nDesconto Inss:{desconto_inss}\nNovo Salario:{novo_salario}'  

def menu():
    while True:
        print('\n=============================')
        print('BONUS E DESCONTOS DO SALARIO'\
              '\n0 - ENCERRA O PROGRAMA')
        print('=============================')

        salario = float(input('Digite seu salario: '))
        if salario == 0:
            print('Encerrando o programa...')
            break
        print(bonus_auxilio_inss(salario))



menu()
