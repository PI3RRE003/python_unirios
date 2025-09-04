'''
lista_a=[4,2,8,6,5]
lista_b = lista_a
lista_b[3] = 999
print(lista_a)

lista_a=[4,2,8,6,5]
lista_b = lista_a[:]
lista_b[3] = 999
print(lista_a)
'''

'''
uma_lista = [3.67, "gato", [56.57, "cachorro"], [], 3.14, False]
print(uma_lista[4:])
'''
'''
uma_lista = [3,67, "gato", 3.14, False]
print(len(uma_lista))
outra_lista = [3,67, "gato", [56.57, "cachorro"], False]
print(len(outra_lista))
'''
'''
uma_lista=[1,3,5]
outra_lista=[2,4,6]
print(uma_lista + outra_lista)

uma_lista = [1,3,5]
print(uma_lista*3)
'''
'''
lista = [0]*10
for i in range(len(lista)):
    lista[i] = i *2

print(0 in lista)
print(1 in lista)
print(2 in lista)
print(3 in lista)
print(4 in lista)
'''

lista = [5, 7, 3, 6]
pos = 2
for i in range(len(lista)-1, pos-1, -1):
    lista[i] = lista[i-1]
lista[pos - 1] = 8
print(lista)