palavras = ["python", "java", "python", "c"]
def contar_ocorrencias(lista):
    contagem = {}
    for palavras in lista:
        contagem[palavras] = contagem.get(palavras, 0) + 1
    return contagem


print(contar_ocorrencias(palavras))