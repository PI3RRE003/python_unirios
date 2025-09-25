nomes = ['vitor', 'kawane']

for nome in nomes:
    if nome[1] == 'kawane':
        n = input("Digite um novo nome")
        nome[1] = n
        print(f"Nome atualizado: {nome[1]}")

