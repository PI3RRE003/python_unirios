def soma(n1, n2):
    soma = n1 + n2
    return f'Soma:{soma}'

def raiz_quadrada(numero):
    raiz = numero ** 0.5
    return f'Raiz:{raiz}'

def potenciacao(base,expoente):
    potencia = base ** expoente
    return f'Potencia:{potencia}'



def menu():
    while True:
        print('\n==============================='\
              '\nMenu Opções:'\
              '\n1. Soma de dois numeros.'\
              '\n2. Raiz Quadrada de um número.'\
              '\n3. Potência de um Número.'\
              '\n0. Sair')
        
        print('=================================')
        op = int(input('Digite a opção desejada:'))

        if op == 1:
            numero_1 = float(input('Digite 1 numero:'))
            numero_2 = float(input('Digite 2 numero:'))
            print(soma(numero_1, numero_2))
        elif op == 2:
            numero = float(input('Digite um numero: '))
            print(raiz_quadrada(numero))
        elif op == 3:
            base = int(input('Digite a base: '))
            expoente = int(input('Digite expoente: '))
            print(potenciacao(base, expoente))
        elif op == 0:
            print('Encerrando o programa....')
            break


menu()