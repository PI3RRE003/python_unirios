print('Calcula salario')
salario = float(input('Digite seu salario: '))

if salario <= 600:
    auxilio_escola = 150
elif salario > 600:
    auxilio_escola = 100

if salario < 500:
    bonus = 0.05
    sal_bonificado = (salario*bonus) +salario
    novo_salario = salario + (salario*bonus) + auxilio_escola
elif salario >= 500 and salario < 1200:
    bonus = 0.12
    sal_bonificado = (salario*bonus) +salario
    novo_salario = salario + (salario*bonus) + auxilio_escola
elif salario > 1200:
    sal_bonificado = 'Sem Bonificação'
    bonus = 'Sem Bonificação'
    novo_salario = salario + auxilio_escola


print(f'Salario:{salario}\nBonus:{bonus}\nsalario Bonificado:{sal_bonificado}\nauxilio escola:{auxilio_escola}\nNovo salario:{novo_salario}')