lista_original = []
for i in range(1,11):
    n = int(input(f'Digite {i} numero: '))
    lista_original.append(n)

print(lista_original)

qtd = 0
lista_50 = []

for j in lista_original:
    if j > 50:
        lista_50.append(j)
    if j < 10:
        qtd += 1

print(f'Numeros maiores que 50:{lista_50}\nNumeros menores que 10:{qtd}')