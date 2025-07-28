numeros_inteiros = []
numeros_impares = []
numeros_pares = []

for i in range(1, 21):
    numero = int(input(f'Digite {i} numero:'))
    numeros_inteiros.append(numero)
    if numero % 2 == 0:
        
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print(f'Numeros Inteiros: {numeros_inteiros}')
print(f'Numeros Impares: {numeros_impares}')
print(f'Numeros Pares: {numeros_pares}')