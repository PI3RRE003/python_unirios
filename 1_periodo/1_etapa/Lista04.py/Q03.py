sexo_m = 0
sexo_f = 0

for i in range(1,4):
    sexo = input(f'Digite {i} Sexo\nM - Masculino\nF - Feminino\n:')

    if sexo == 'M' or sexo == 'm':
        sexo_m +=1
    elif sexo == 'F' or sexo == 'f':
        sexo_f +=1

print(f'Pessoas do sexo masculino:{sexo_m}')
print(f'Pessoas do sexo feminino:{sexo_f}')