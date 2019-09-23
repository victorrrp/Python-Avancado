'''
Métodos estáticos
'''
from random import randint 

class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    '''
    método sem decorador - método de instância que precisa receber 
    o decorador que se refere a própria instância(self)
    '''
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    
    '''
    método de classe - precisa estar decorado com classmethod 
    e ele não é referente à instancia em si, mas à classe
    '''
    @classmethod 
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    '''
    método estático - é tratado como uma função normal mesmo estando dentro
    da classe. não pode utilizar a instância nem a classe em seu interior
    '''
    @staticmethod 
    def gera_id():
        rand = randint(10000, 19999)
        return rand

#p1 = Pessoa.por_ano_nascimento('Victor', 1997)
p1 = Pessoa('Victor', 22)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
