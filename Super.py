#SISTEMA DE ESCOLA
#CLASSES: ALUNO, PROFESSOR, ASSISTENTE

class Aluno():
    def __init__(self, nome, idade, ano):
        self.nome = nome
        self.idade = idade
        self.ano = ano
    def apresentar(self):
        print(f'Meu nome é {self.nome} e eu sou um aluno do {self.ano}º ano.')

class Professor():
    def __init__(self, nome, idade, materia): 
        self.nome = nome
        self.idade = idade
        self.materia = materia
    def apresentar(self):
        print(f'Meu nome é {self.nome} e eu sou professor de {self.materia}.')

class Assistente():
    def __init__(self, nome, idade, bloco):
        self.nome = nome
        self.idade = idade
        self.bloco = bloco
    def apresentar(self):
        print(f'Meu nome é {self.nome} e eu sou assistente do {self.bloco}.')

ps1 = Professor('Roberto', 34, 'Matemática')
ps1.apresentar()

as1 = Assistente('Andre', 21, 'Bloco A')
as1.apresentar()