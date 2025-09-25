class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'O meu nome é {self.nome} e tenho {self.idade} de idade')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome,idade)
        self.cargo = cargo

    def trabalhar(self):
        print(f'{self.nome} esta trabalhando como {self.cargo}!')

class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome,idade)
        self.saldo = saldo

    def comprar(self, valor_compra):
        if valor_compra <= self.saldo:
            self.saldo -= valor_compra
            print(f'A sua compra de {valor_compra} reais foi Aprovada! Seu saldo atual é de: R${self.saldo}')
        else:
            print(f'Saldo insuficiente')



pessoa1 = Pessoa('Andre', 13)
#pessoa1.apresentar()

f1 = Funcionario('Maria', 38, 'Analista de suporte')
#f1.trabalhar()

cliente1 = Cliente('Yasmin', 16, 200)
#cliente1.apresentar()
cliente1.comprar(300)
