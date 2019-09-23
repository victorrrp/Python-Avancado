'''
Atributos (ou variáveis) de classe
'''
class A:
    vc = 123 #variável da classe

    def __init__(self):
        self.vc = 321 #variável de instância pré determinando o valor abaixo

#instâncias da classe
a1 = A()
a2 = A() 

print(a1.vc)
print(a2.vc)

#é possivel imprimir a variavel da classe sem instancia-la
print(A.vc)

#para modificar a variável de classe, pode-se usar a própria classe para este fim
#A.vc = 321