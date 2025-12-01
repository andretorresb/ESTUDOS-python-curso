
class Personagens():
    def falar(self):
        print('Eu sou um personagem.')

class Guerreiro(Personagens):
    def falar(self):
        print('Eu sou um guerreiro!')

class Mago(Personagens):
    def falar(self):
        print('Eu sou um mago!')

class Arqueiro(Personagens):
    def falar(self):
        print('Eu sou um arqueiro!')

#Criar os objetos

personagens = [Guerreiro(), Mago(), Arqueiro()]
for p in personagens:
    p.falar()