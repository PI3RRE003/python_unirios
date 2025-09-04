def positivo_negativo(num):
    if num < 0:
        return 'Negativo'
    elif num > 0:
        return 'Positivo'
    else:
        return 'NULL'
    

num = int(input('Digite um numero: '))
print(positivo_negativo(num))