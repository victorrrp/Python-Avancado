'''
Agregação - Tipo de relação em POO que uma classe usa outra classe 
como parte de si e elas precisam uma da outra
'''

class CarrinhoDeCompras: #esta classe pode existir sozinha mas necessita, no caso, dos produtos
    def __init__(self): #método de classe
        self.produtos = [] #atributo de instância
    
    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self): #construindo uma variável de cálculo
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total 

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor