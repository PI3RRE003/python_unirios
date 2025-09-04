def mostrar_totais(estados):
    for estado, qtd in estados.items():
        # if estado == estado:
        #     qtd += qtd
        print(f'{estado} - {qtd}')

def estado_com_mais_hospedes(estado):
    mais_hospedes = 0
    for estado, qtd in estados.items():
        if qtd > mais_hospedes:
            mais_hospedes = qtd
    print(f'Estado com mais hospedes: {estado} - Quantidade: {mais_hospedes}')
estados = {}
for i in range(1,3):
    print('\nEstado de origem\
                    \nAL\
                    \nBA\
                    \nPE\
                    \nSP')
    estado = input('Digite a opção: ').upper()
    qtd_hospedes = int(input('Digite a quantidade de hospedes: '))
    estados[estado] = qtd_hospedes

mostrar_totais(estados)
estado_com_mais_hospedes(estado)