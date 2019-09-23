'''
Herança Simples - Quando o objeto é o outro objeto
'''

class Pessoa: #superclasse. todos os métodos pertencentes a esta classe, pertence tambem as que estiverem fora dela
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nomeclasse} falando...')


#classes herdeiras ou subclasses. nada impede deles terem seus métodos especificos
class Cliente(Pessoa):
    def comprar(self): #este método pertence somente a Cliente
        print(f'{self.nomeclasse} comprando...')

class Aluno(Pessoa):
    def estudar(self): #este método pertence somente a Aluno
        print(f'{self.nomeclasse} estudando...')