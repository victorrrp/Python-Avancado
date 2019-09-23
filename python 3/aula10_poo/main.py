from classes import Cliente
from classes import Pessoa
from classes import Aluno

c1 = Cliente('Victor', 22)
print(c1.nome)
c1.comprar() #instancia única da classe filha
c1.falar() #instancia de todos pois está na superclasse
print()

a1 = Aluno('Joana', 52)
print(a1.nome)
a1.estudar() #instancia única da classe filha
a1.falar() #instancia de todos pois está na superclasse
print()


#é possivel instanciar somente a classe 'mãe' sem que as outras interfiram.
#na hierarquia, a herança vem de cima pra baixo
p1 = Pessoa('João', 43)
p1.falar()