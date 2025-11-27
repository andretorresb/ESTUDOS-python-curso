class Biblioteca:
    def __init__(self, titulo, autor, pagina, disponivel: True):
        self.titulo = titulo
        self.autor = autor
        self.pagina = pagina
        self.disponivel = disponivel

class Partilheira:
    def __init__(self):
        self.livros = []

    def livros_adicionar(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            status = 'Disponivel' if livro.disponivel else "Indisponivel"
            print(f'Titulo: {livro.titulo} - Autor: {livro.autor} e tem {livro.pagina} paginas!, Status {status}')

## Objetos

python = Biblioteca('Python do zero', 'Andre limo', 32, True)
java = Biblioteca('Java', 'Andre limo', 55, False)

#Objeto - adicionar na class Biblioteca

partilheira = Partilheira()
partilheira.livros_adicionar(python)
partilheira.livros_adicionar(java)

#listar - O objeto adicionado
partilheira.listar_livros()