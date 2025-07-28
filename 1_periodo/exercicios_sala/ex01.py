meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro", "Dezembro"]

chuvas = []
for mes in meses:
    valor = float(input(f'Chuva em {mes}(mm): '))
    chuvas.append(valor)

media_anual = sum(chuvas)/12
mais_chuva = meses[chuvas.index(max(chuvas))]
menos_chuva = meses[chuvas.index(min(chuvas))]
acima_media=0 

for mes in chuvas:
    if mes > media_anual:
        acima_media += 1
        
print(f'O mes mais chuvoso foi:{mais_chuva}')
print(f'O mes menos chuvoso foi:{menos_chuva}')
print(f'A media anual foi de {media_anual:.2f}mm')
print(f'Tiveram {acima_media} meses acima da media anual')