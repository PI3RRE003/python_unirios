print('Categoria de nadadores')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade >= 5 and idade <= 7:
    print(f'Nome:{nome}\nIdade:{idade}\nCategoria: Infantil A')
elif idade >= 8 and idade <= 10:
    print(f'Nome:{nome}\nIdade:{idade}\nCategoria: Infantil B')
elif idade >= 11 and idade <= 13:
    print(f'Nome:{nome}\nIdade:{idade}\nCategoria: Juvenil A')
elif idade >= 14 and idade <= 17:
    print(f'Nome:{nome}\nIdade:{idade}\ncategoria: Juvenil B')
elif idade >= 18:
    print(f'Nome:{nome}\nIdade:{idade}\ncategoria: Sênior')