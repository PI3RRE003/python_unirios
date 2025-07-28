numero_par = 0
numero_impar = 0

for i in range(1,11):
    numero = int(input('Digite um numero inteiro: '))

    if numero % 2 == 0:
        numero_par += 1
    else:
        numero_impar += 1

print(f'Quantidade de Numeros pares digitados:{numero_par}')
print(f'Quantidade de Numeros impares digitados:{numero_impar}')
