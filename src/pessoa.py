class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fala_algo(self):
        return f'Oi! Meu nome é {self.nome}.'