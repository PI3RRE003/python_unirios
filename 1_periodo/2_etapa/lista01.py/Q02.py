while True:
    print('CALCULA IPTU ATRASADO')
    registro = int(input('Número do registro na prefeitura:'))
    imposto = float(input('Valor do imposto:'))
    atraso = int(input('Número de meses em atraso:'))

    if imposto <= 500:
        percentual = 0.01
        multa = (imposto*percentual) * atraso
        novo_imposto = imposto + multa
    elif imposto > 500 and imposto <= 1800:
        percentual = 0.02
        multa = (imposto*percentual) * atraso
        novo_imposto = imposto + multa
    elif imposto > 1800 and imposto <= 5000:
        percentual = 0.04
        multa = (imposto*percentual) * atraso
        novo_imposto = imposto + multa
    elif imposto > 5000 and imposto <= 12000:
        percentual = 0.07
        multa = (imposto*percentual) * atraso
        novo_imposto = imposto + multa
    elif imposto > 12000:
        percentual = 0.10
        multa = (imposto*percentual) * atraso
        novo_imposto = imposto + multa
    else:
        print('ERRO')
        break

    print(f'\nRegistro do imóvel:{registro}\nMulta:{multa:.2f}\nMeses em atraso:{atraso:.2f}\nNovo Imposto:{novo_imposto}\n')