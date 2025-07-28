al = []
ba = []
pe = []
sp = []
for hospede in range(1,6):
    print(f'{hospede}. Hospede')
    estado = input('Estado de origem\
                    \nAL\
                    \nBA\
                    \nPE\
                    \nSP\
                    \nDigite a opção: ')
    
    if estado.upper() == 'AL':
        al.append(estado)
    elif estado.upper() == 'BA':
        ba.append(estado)
    elif estado.upper() == 'PE':
        pe.append(estado)
    elif estado.upper == 'SP':
        sp.append(estado)

total_al = len(al)
total_ba = len(ba)
total_pe = len(pe)
total_sp = len(sp)

print(f'\nTotal de hospedes Alagoas: {total_al}')
print(f'Total de hospedes Bahia: {total_ba}')
print(f'Total de hospedes Pernambuco: {total_pe}')
print(f'Total de hospedes São Paulo: {total_sp}')

if len(al) > len(ba) and len(al) > len(pe) and len(al) > len(sp):
    print(f'\nEstado com maior número de hospedes: Alagoas')
elif len(ba) > len(al) and len(ba) > len(pe) and len(ba) > len(sp):
    print(f'\nEstado com maior número de hospedes: Bahia')
elif len(pe) > len(al) and len(pe) > len(ba) and len(pe) > len(sp):
    print(f'\nEstado com maior número de hospedes: Pernambuco')
elif len(sp) > len(al) and len(sp) > len(ba) and len(sp) > len(pe):
    print(f'\nEstado com maior número de hospedes: São Paulo')