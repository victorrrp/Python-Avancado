'''  
Property - decorador
Getters - Obtém (filtra) um valor 
Setters - Configura o valor do getter valor. 
pode-se considerar que são "proteções" aos atributos sem alterar a estrutura da classe
'''

class Produto:
 
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    #Criando um Getter
    @property
    def preco(self):
        return self._preco

    #Criando um Setter
    @preco.setter
    def preco(self, valor): #o 'valor' será atribuído à variável preço no início do código
        if isinstance(valor, str): #checando se o valor é uma instância de str (string)
            valor = float(valor.replace('R$', '')) #casting de str para float
        
        self._preco = valor


p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Blusa mengão', 'R$250') #string erro a fim de exemplificar a resolução
p2.desconto(15)
print(p2.preco)