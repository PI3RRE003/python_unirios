numeros = []

def menor_numero_da_lista():
    menor_numero = numeros[0]
    for numero in numeros[1:]:
        if numero < menor_numero:
            menor_numero = numero
    print(menor_numero)

def maior_numero_da_lista():
    maior_numero = numeros[0]
    for numero in numeros:
        if  maior_numero < numero:
            maior_numero = numero
    print(f'Maior numero:{maior_numero}')
    
def soma_pares():
    numero_par = 0
    for numero in numeros:
        if numero % 2 == 0:
            numero_par += numero
    print(f'A soma de todos pares é:{numero_par}')

def quantidade_de_impares():
    qtd_impares = 0
    for numero in numeros:
        if numero % 2 == 1:
            qtd_impares += 1
    print(f'A quantidade de impares na lista é: {qtd_impares}') 
        

def menu():
    while True:
        print('\n========== ANALISE DE NUMEROS ==========')
        print('1 - O MENOR NUMERO DA LISTA\
              \n2 - O MAIOR NUMERO DA LISTA\
              \n3 - A SOMA DE TODOS PARES\
              \n4 - A QUANTIDADE DE NUMEROS IMPARES\
              \n5 - ADICIONAR NUMEROS A LISTA\
              \n0 - Sair\
              \n==========================================')
        
        op = int(input('Digite a opção: '))
        if op == 1:
            if not numeros:
                print('Lista vazia, adicione numeros na opção 5')
            else:
                menor_numero_da_lista()
        elif op == 2:
            maior_numero_da_lista()
        elif op == 3:
            soma_pares()
        elif op == 4:
            quantidade_de_impares()
        elif op == 5:
            for i in range(1, 11):
                numero = int(input(f'Digite {i}° numero: '))
                numeros.append(numero)
            print(f'Numeros adicionado a lista:{numeros}')
        elif op == 0:
            print('Encerrando o programa...')
            break


menu()