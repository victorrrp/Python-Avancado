class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereços = []

#executando a composição de classes
    def insere_endereço(self, cidade, estado):
        self.endereços.append(Endereço(cidade, estado))

    def lista_endereços(self):
        for endereço in self.endereços:
            print(endereço.cidade, endereço.estado)

class Endereço:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado