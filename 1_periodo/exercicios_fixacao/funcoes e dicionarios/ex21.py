def media_nota(notas):
    media = sum(notas) / len(notas)  
    return media

media_final = media_nota([5,5,5])
print(media_final)