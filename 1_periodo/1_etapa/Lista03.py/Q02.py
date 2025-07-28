print('Classificação por peso')
nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

if altura < 1.20 and peso <= 60:
    print(f'\nNome:{nome}\nAltura:{altura}\nPeso:{peso}\nCategoria:A')
elif altura >= 1.20 and altura < 1.70 and peso <= 60:
    print(f'\nNome:{nome}\nAltura:{altura}\nPeso:{peso}\nCategoria:B')
elif altura >= 1.70 and peso <= 60:
    print(f'\nNome:{nome}\nAltura:{altura}\nPeso:{peso}\nCategoria:C')
elif altura < 1.20 and peso > 60 and peso < 90:
    print(f'\nNome:{nome}\nAltura:{altura}\nPeso:{peso}\nCategoria:D')
elif altura >= 1.20 and altura < 1.70 and peso > 60 and peso < 90:
    print(f'\nNome:{nome}\nAltura:{altura}\nPeso:{peso}\nCategoria:E')
elif altura >= 1.70 and peso > 60 and peso < 90:
    print(f'\nNome:{nome}\nAltura:{altura}\nPeso:{peso}\nCategoria:F')
elif altura < 1.20 and peso > 90:
    print(f'\nNome:{nome}\nAltura:{altura}\nPeso:{peso}\nCategoria:G')
elif altura >= 1.20 and altura < 1.70 and peso > 90:
    print(f'\nNome:{nome}\nAltura:{altura}\nPeso:{peso}\nCategoria:H')
elif altura > 1.70 and peso > 90:
    print(f'\nNome:{nome}\nAltura:{altura}\nPeso:{peso}\nCategoria:I')
