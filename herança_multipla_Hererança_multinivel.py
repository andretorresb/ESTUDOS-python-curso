#herança multipla e Hererança multinivel

#Classe Avo
class Animal():
    def __init__(self, nome):
        self.nome = nome


#Classe Pai
class Predador(Animal):
    def cacando(self):
        print(f"O animal {self.nome} esta caçando...")

class Presa(Animal):
    def fugindo(self):
        print(f"O animal {self.nome} está correndo...")

#Classes Filhos
class Coelho(Presa):
    pass

class Tigre(Predador):
    pass

class Golfinho(Predador, Presa):
    pass

coelho1 = Coelho("Coelho")
tigre1 = Tigre("Tigre")
golfilho1 = Golfinho("Golfinho")

golfilho1.cacando()
coelho1.fugindo()
tigre1.cacando()