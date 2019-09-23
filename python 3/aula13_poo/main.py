'''
Classes abstratas - Geralmente é utilizada quando cria-se uma classe genérica caso não queira que ela seja instanciada
Pode ter metodos concretos e métodos abstratos


#chamando uma classe básica abstrata (abc - sigla em ingles)

from abc import ABC, abstractmethod


#exemplo de classe sendo instanciada 
class A(ABC):
    pass

a = A()


#proibindo que a classe seja instanciada. permitindo apenas que sirva como base para outras classes

class A(ABC):
    @abstractmethod
    def falar(self):
        pass

class B(A):
    def falar(self):
        print('Falando... B...')

a = A()
a.falar()

'''

from classes.cp import ContaPoupanca
from classes.cc import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(10) #se o valor de sacar for maior que o depositado, aparecerá "Saldo insuficiente"

print('###########################')

cc = ContaCorrente(1111, 3333, 0, 500)

cc.depositar(100)
cc.sacar(250)
cc.sacar(500)

cc.depositar(500000)
cc.sacar(80000)
