#criar um Aggregation, refiz tudo

class Bibiloteca:
    def __init__(self, titulo, autor, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel
    
class Partilheira:
    def __init__(self):
        self.livros = []

    def adiciona_livros(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            status = 'Disponivel' if livro.disponivel else 'Indisponivel'
            print(f' Titulo: {livro.titulo} - Autor: {livro.autor} - Status {status}')
        

python = Bibiloteca('Python do zero', 'Andre lindo', True)

partilheira = Partilheira()
partilheira.adiciona_livros(python)

partilheira.listar_livros()