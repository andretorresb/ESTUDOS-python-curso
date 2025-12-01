#SISTEMA DE ESCOLA
#CLASSES: ALUNO, PROFESSOR, ASSISTENTE

class Escola(): 
    def __init__(self, nome, idade, status, ano):
        self.nome = nome
        self.idade = idade
        self.status = status
        self.ano = ano

    def apresentar(self):
        print(f'Olá, meu nom é {self.nome}')
    
    def verificar_status(self):
        print(f'Status: {"Ativo" if self.status else "Inativo"}')

class Aluno(Escola):
    def __init__(self, nome, idade, status, ano):
        super().__init__(nome, idade, status, ano)
    
    def apresentar(self): 
        print(f'Ola, meu nome é {self.nome} e eu tenho {self.idade} anos.')

class Professor(Escola):
    def __init__(self, nome, idade, status, ano, materia): 
        super().__init__(nome, idade, status, ano)
        self.materia = materia

class Assistente(Escola):
    def __init__(self, nome, idade, status, ano, bloco):
        super().__init__(nome, idade, status, ano)
        self.bloco = bloco
    

a1 = Aluno('Weverton', idade=20,status=True, ano=3)
a1.apresentar()
a1.verificar_status()

ps1 = Professor('Roberto', 34, False, 5, 'Matemática')
ps1.apresentar()
ps1.verificar_status()

as1 = Assistente('Andre', 21, True, 2, 'Bloco A')
as1.apresentar()
as1.verificar_status()