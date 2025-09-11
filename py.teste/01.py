idade_total = int(input('Digite sua idade:  '))
salario = float(input('Digite seu salário:  '))

if idade_total > 21 and salario > 2000:
    print('Você pode fazer o emprestimo')
elif idade_total > 21 and salario < 2000:
    print('Seu credito e muito baixo ')
elif idade_total < 21 and salario > 2000:
    print('Você não esta comprindo uma das regras adequadas')
elif idade_total < 21 and salario < 2000:
    print('Infelizmente você não pode ser nosso cliente')
