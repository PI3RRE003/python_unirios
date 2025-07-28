print('Conversor dolar, euro')
real = float(input('Digite valor em R$: '))
dolar = real / 5.04  
euro = real / 5.32  

print(f'Cotação:\nReal:{real}\nDolar:{dolar:.2f}\nEuro:{euro:.2f}')