def temperaturas_registradas(temperatura_semanal):
    return f'Temperaturas registradas na semana:{temperatura_semanal}'

def calcula_media_temperatura(temperatura_semanal):
    media = sum(temperatura_semanal)/len(temperatura_semanal)
    return f'\nMédia temperatura da semana:{media:.2f}'

def temperaturas_acima_30(temperatura_semanal):
    acima_30 = []
    for temperatura in temperatura_semanal:
        if temperatura >= 30:
            acima_30.append(f'{temperatura}°')
    return f'\nTemperaturas acima de 30°: {acima_30}'

temperatura_semanal = []

def menu():
    for i in range(1,4):
        print(f'{i} Dia semana:')
        temperatura = float(input('Digite a temperatura diaria: '))
        temperatura_semanal.append(temperatura)

menu()
print(temperaturas_registradas(temperatura_semanal=temperatura_semanal))
print(calcula_media_temperatura(temperatura_semanal=temperatura_semanal))
print(temperaturas_acima_30(temperatura_semanal=temperatura_semanal))