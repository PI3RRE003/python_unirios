def dobra_numeros(*valor):
    numeros = []
    for numero in valor:
        numeros.append(numero*2)
    return numeros


print(dobra_numeros(1,2,3))