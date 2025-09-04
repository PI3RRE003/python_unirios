def imprimir():
    print(f'Olá mundo')

def imprimir2(frase):
    print(frase)

def soma(n1,n2):
    return n1 + n2

def potencia(numero, expoente):
    return numero**expoente

def tipoNumero(numero):
    if numero % 2 == 0:
        n = f'Numero:{numero} e par'
    else:
        n = f'Numero:{numero} e impar'
    return n
'''
imprimir()
imprimir2('Boa noite')

'''
'''
n1 = int(input('Digite 1 numero: '))
n2 = int(input('Digite 2 numero: '))
print(f"Soma:{soma(n1,n2)}")
print(f'Potencia:{potencia(n1,n2)}')
'''
numero = int(input("Digite um numero para descobrir se e impar ou par: "))
print(tipoNumero(numero))