abaixo_do_peso = []
saudavel = []
peso_em_execesso = []
obesidade_1 = []
obesidade_2 = []
obesidade_3 = []




for i in range(1,2):
    nome = input('Digite seu nome: ')
    altura = float(input('Digite sua alturam em Metros: '))
    peso = float(input('Digite seu peso em Kg: '))

    imc = peso/altura**2

    if imc < 18.5:
        abaixo_do_peso.append((nome, imc))
        print(f'Nome:{nome}\nIMC:{imc}\nClassificação: Abaixo do peso\n')
    elif imc >= 18.5 and imc <= 24.9:
        saudavel.append((nome,imc))
        print(f'Nome:{nome}\nIMC:{imc}\nClassificação: Saudavel\n')
    elif imc >= 25 and imc <= 29.9:
        peso_em_execesso.append((nome,imc))
        print(f'Nome:{nome}\nIMC:{imc}\nClassificação: Peso em excesso\n')
    elif imc >= 30 and imc <= 34.9:
        obesidade_1.append((nome,imc))
        print(f'Nome:{nome}\nIMC:{imc}\nClassificação: Obesidade Grau I\n')
    elif imc >= 35 and imc <= 39.9:
        obesidade_2.append((nome,imc))
        print(f'Nome:{nome}\nIMC:{imc}\nClassificação: Obesidade Grau II\n')
    elif imc >= 40:
        obesidade_3.append((nome,imc))
        print(f'Nome:{nome}\nIMC:{imc}\nClassificação: Obesidade Grau III\n')
    else:
        print('erro')    


print('========== RESULTADOS ==========')
if not abaixo_do_peso:
    print('Classificação: Abaixo do peso:')
    print('Sem registro')
else:
    print('Classificação: Abaixo do peso:')
    print('Nome e IMC')
    for i in range(len(abaixo_do_peso)):
        print(f'{abaixo_do_peso[i]}')

if not saudavel:
    print('\nClassificação: Saudavel')
    print('Sem registro')
else:
    print('\nClassificação: Saudavel')
    print('Nome e IMC')
    for i in range(len(saudavel)):
        print(f'{saudavel[i]}')

if not peso_em_execesso:
    print('\nClassificação: Peso em exesso')
    print('Sem registro')
else:
    print('\nClassificação: Peso em exesso')
    print('Nome e IMC')
    for i in range(len(peso_em_execesso)):
        print(f'{peso_em_execesso[i]}')

if not obesidade_1:
    print('\nClassificação: Obesidade I')
    print('sem registro')
else:
    print('\nClassificação: Obesidade I')
    print('Nome e IMC:')
    for i in range(len(obesidade_1)):
        print(f'{obesidade_1[i]}')

if not obesidade_2:
    print('\nClassificação: Obesidade II')
    print('Sem registro')
else:
    print('\nClassificação: Obesidade II')
    print('Nome e IMC:')
    for i in range(len(obesidade_2)):
        print(f'{obesidade_2[i]}')

if not obesidade_3:
    print('\nClassificação: Obesidade III')
    print('Sem registro')
else:
    print('\nClassificação: Obesidade III')
    print('Nome e IMC:')
    for i in range(len(obesidade_3)):
        print(f'{obesidade_3[i]}')