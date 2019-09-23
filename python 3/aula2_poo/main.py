#métodos de classes

class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self): #método de classe
        print(self.ano_atual - self.idade)
    

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

#p1 = Pessoa.por_ano_nascimento('Victor', 1997)
p1 = Pessoa('Victor', 22)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

'''
Quando devo utilizar um método de instância ou um método de classe?
O primordial é saber se o que você está criando
é relacionado à classe, ao molde em geral
ou a instância, especificando o objeto 
'''