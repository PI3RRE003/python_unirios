class MusicaDuplicadaError(Exception):
    pass

class PlaylistVaziaError(Exception):
    pass

class Musica:
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        minutos, segundos = divmod(self.duracao, 60)
        return f"Musica: {self.titulo} \nArtista: {self.artista} \nDuração: {self.duracao:.2f}s"

class Playlist:
    def __init__(self, nome, musicas=None):
        self.nome = nome
        if musicas is None:
            self.musicas = []
        else:
            self.musicas = musicas

    def adicionar_musica(self,musica_nova):
        for musica_existente in self.musicas:
            if (musica_existente.titulo ==  musica_nova.titulo and
                musica_existente.artista == musica_nova.artista):
                raise MusicaDuplicadaError(f"A musica: {musica_nova.titulo} já esta na playlist")

        self.musicas.append(musica_nova)
        print(f"Adicionada: `{musica_nova}")

    def tocar_proxima(self):
        if not self.musicas :
            raise PlaylistVaziaError("Playlist Vazia, adicione uma musica")
        else:
            return self.musicas.pop(0)

    def __str__(self):
        return f"Playlist: {self.nome}\nMusicas: {self.musicas}"
        
    
m1 = Musica("Só quando ela me quer", "Yunk vino", 1.5)
print(m1)