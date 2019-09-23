#Relacionamento entre classes por associação
#Como os atributos são privados, é necessário utlizar o setter e o getter

class Escritor:
    def __init__(self, nome):
        self.__nome = nome #(__nome == setter)
        self.__ferramenta = None #atributo de instância pronto para receber qualquer valor

    @property #getter para nome
    def nome(self):
        return self.__nome
    
    @property #getter para ferramenta
    def ferramenta(self):
        return self.__ferramenta  

    @ferramenta.setter 
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca
    
    def escrever(self):
        print('Caneta está escrevendo...')

    @property 
    def marca(self):
        return self.__marca
    
class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')