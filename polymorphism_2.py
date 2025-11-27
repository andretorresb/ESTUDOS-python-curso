class Pessoa1:
    def emitir_som(self):
        print('Meu nome é joão!')

class Pessoa2:
    def emitir_som(self):
        print('Meu nome é maria!')

pessoas = [Pessoa1(), Pessoa2()]
for p in pessoas:
    p.emitir_som()