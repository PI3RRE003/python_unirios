def contar_letras(palavra):
    contagem = {}
    for letra in palavra:
        '''
        if letra in contagem:
          contagem[letra]+=1
        else:
          contagem[letra] = 1
        '''
        contagem[letra] = contagem.get(letra, 0) + 1
    return contagem

print(contar_letras('Vitor'))