abaixo_peso = []
saudavel = []
peso_exesso = []
obesidade = []

for i in range(1,3):
    nome = input('\nDigite seu nome: ')
    altura = float(input(f'{nome}, digite sua altura: '))
    peso = float(input(f'{nome}, digite seu peso: '))

    imc = peso/altura**2

    if imc < 18.5:
        abaixo_peso.append(nome)
        abaixo_peso.append(imc)
    elif imc >= 18.5 and imc <= 24.9:
        saudavel.append(nome)
        saudavel.append(imc)
    elif imc >= 25 and imc <= 29.9:
        peso_exesso.append(nome)
        peso_exesso.append(imc)
    elif imc >= 30 and imc <= 34.9:
        mensagem = 'Obesidade grau 1'
        obesidade.append(mensagem)
        obesidade.append(nome)
        obesidade.append(imc)
    elif imc >= 35 and imc <= 39.9:
        mensagem = 'Obesidade grau 2'
        obesidade.append(mensagem)
        obesidade.append(nome)
        obesidade.append(imc)
    elif imc >= 40:
        mensagem = 'Obesidade grau 3'
        obesidade.append(mensagem)
        obesidade.append(nome)
        obesidade.append(imc)

print(f'Pessoas abaixo do peso: {abaixo_peso}\n')
print(f'\nPessoas saudaveis:{saudavel}\n')
print(f'\nPessoas com peso em exesso:{peso_exesso}\n')
print(f'\nPessoas obesas: {obesidade}\n')