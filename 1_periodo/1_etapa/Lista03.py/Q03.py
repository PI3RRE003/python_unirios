print('Condição aposentadoria')
idade = int(input('Digite sua idade: '))
tempo_servico = int(input('Digite seu tempo de serviço: '))

if idade >= 65:
    print(f'Aposenta por causa da idade: {idade}')
elif idade > 60 and tempo_servico > 25:
    print(f'Aposenta por cauda da idade:{idade} e tempo de serviço: {tempo_servico} ')
elif idade < 65 and tempo_servico >= 30:
    print(f'Aponseta pelo tempo de serviço:{tempo_servico}')