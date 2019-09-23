'''
Métodos mágicos. Por convenção, são métodos que começam e terminam com dois underlines
De forma geral, eles modificam o comportamento de sua classe
'''

class A:
    def __init__(self): #método mágico inicializador
        print('Eu sou o INIT')


a = A()