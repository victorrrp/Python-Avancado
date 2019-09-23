'''
Encapsulamento em POO - Serve para 'esconder' certas partes do seu
código para 'proteger' sua aplicação (seja classe, atributo ou método)
Métodos e atributos public - podem ser acessados dentro e fora da classe
Métodos e atributos protected - podem ser acessados somente dentro da classe ou das filhas daquela classe
Métodos e atributos private - só está disponível dentro da classe
'''

#modificadores de acesso

class BaseDeDados:
    
    def __init__(self):
        self.dados = {} #dicionário público. colocando um _ ex '_dados', torna-se protected e sugerindo que não seja acessado

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome} #criando o dicionário (dados)
        else:
            self.dados['clientes'].update({id:nome}) #atualizando o dicionário para ser inserido novos clientes

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Victor')
bd.inserir_cliente(2, 'Otávio')
bd.inserir_cliente(3, 'Luiz')
bd.apaga_cliente(2)
