from abc import ABC, abstractmethod


class Conta(ABC): #esta classe tem que herdar de ABC, pois é a classe abstrata
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)): #checando se 'valor' é uma instância de int ou float
            raise ValueError("Saldo precisa ser numérico")
        
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do deposito precisa ser numérico")
        
        self.saldo += valor
        self.detalhes()
        
    def detalhes(self):
        print(f'Agência: {self.agencia} ',end=' ')
        print(f'Conta: {self.conta} ',end=' ')
        print(f'Saldo: {self.saldo} ')

    @abstractmethod
    def sacar(self, valor):
        pass