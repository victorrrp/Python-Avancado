'''
Sobreposição de membros - Atributos de classes, Atributos de instância e métodos
'''

class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nomeclasse} falando...')


class Cliente(Pessoa):
    def comprar(self): 
        print(f'{self.nomeclasse} comprando...')

class Aluno(Pessoa):
    def estudar(self): 
        print(f'{self.nomeclasse} estudando...')
    
class ClienteVIP(Cliente):
    def falar(self): #neste caso há uma sobre posição modificando o método
        super().falar() #indicando qual método executar primeiro respeitando a hierarquia
        print('Outra coisa qualquer.')


'''
Outra forma de sobrepor é:

class ClienteVIP(Cliente):
    def __init__(self, nome, idade): <-- construtor do ClienteVIP
        Pessoa.__init__(self, nome, idade) <-- construtor de Pessoa (classe mãe)
'''