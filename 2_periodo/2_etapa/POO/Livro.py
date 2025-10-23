class Livro():
    def __init__ (self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano



l1 = Livro("O Senhor dos Aneis", "J.R.R. Tolkien", 1954)
l2 = Livro("Dune", "Frank Herbert", 1965)

print(f"Titulo: {l1.titulo}"
      f"\nAutor: {l1.autor}"
      f"\nAno: {l1.ano}"
      )