while True:
    print('\nCalcula aumento salário por desempenho\n')
    salario = float(input('Digite seu salario:'))
    desempenho = input('Desempenho (A, B, C ou D):')

    if desempenho == 'A' or desempenho == 'a':
        porcentagem = 0.15
        novo_salario = salario + (salario*porcentagem)
        mensagem = f'\nSalário Atual:{salario}\nDesempenho:A (Excelente): 15% de aumento\nNovo salário:{novo_salario}'
    elif desempenho == 'B' or desempenho == 'b':
        porcentagem = 0.10
        novo_salario = salario + (salario*porcentagem)
        mensagem = f'\nSalário Atual:{salario}\nDesempenho:B (Bom): 10% de aumento\nNovo salário:{novo_salario}'
    elif desempenho == 'C' or desempenho == 'c':
        porcentagem = 0.05
        novo_salario = salario + (salario*porcentagem)
        mensagem = f'\nSalário Atual:{salario}\nDesempenho:C (Regular): 5% de aumento\nNovo salário:{novo_salario}'
    elif desempenho == 'D' or desempenho == 'd':
        mensagem = f'\nSalário Atual:{salario}\nDesempenho:D (Insatisfatorio)\nSEM AUMENTO '

    print(mensagem)