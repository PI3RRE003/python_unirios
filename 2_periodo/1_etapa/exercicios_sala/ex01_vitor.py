lista_original = []
lista_maior_50 = []
lista_menor_10 = []
for i in range(1,11):
    print('ARMAZENANDO NÚMEROS:')
    numero = int(input(f'Digite {i} número:'))
    lista_original.append(numero)

    if numero > 50:
        lista_maior_50.append(numero)
    

    if numero < 10:
        lista_menor_10.append(numero) 

    
print(f'Todos os números:{lista_original}')
print(f'Números maiores que 50:{lista_maior_50}')
print(f'Números menores que 10:{lista_menor_10} quantidade:{len(lista_menor_10)}')
