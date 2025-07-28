while True:
    print('Conta energia')
    
    consumo = int(input('Digite seu consumo mensal de kWh:'))
    if consumo <= 100:
        centavo_kwh = 0.50
    elif consumo > 100 and consumo < 300:
        centavo_kwh = 0.70
    elif consumo > 300:
        centavo_kwh = 0.90
    bandeira = input('Bandeira (V, A, V1 ou V2):')
    if bandeira == 'V' or bandeira == 'v':
        tarifa = 0
    elif bandeira == 'A'or bandeira == 'a':
        tarifa = 0.02
    elif bandeira == 'V1' or bandeira == 'v1':
        tarifa = 0.05
    elif bandeira == 'V2' or bandeira == 'v2':
        tarifa = 0.10
    
    valor_total = (consumo*centavo_kwh) + (consumo*tarifa)

    print(f'\nConsumo:{consumo}\nCentavo por kWh:{centavo_kwh}\nBandeira:{bandeira}\nTarifa da bandeira:{tarifa}\nValor total:{valor_total:.2f}\n')