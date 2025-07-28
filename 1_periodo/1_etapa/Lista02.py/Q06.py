print('Nome e senha')
nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

if senha == nome:
    print('senha não pode ser igual a nome')
    print('tente novamente....')
    exit()
else:
    print('Acesso liberado')