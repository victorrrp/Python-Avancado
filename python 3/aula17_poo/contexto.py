'''Gerenciadores de contexto'''


#o problema:

'''
arquivo = open('abc.txt', 'w')
arquivo.write('Alguma coisa')
arquivo.close()
'''

#resolução do problema utilizando o gerenciador de contexto

'''
with open('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')
'''

#criando meu próprio gerenciador de contexto
class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Retornando arquivo')
        return self.arquivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo')
        self.arquivo.close()

with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')

'''
Foi utilizado no exemplo a manipulação de gerenciador de contexto com arquivo
Pode-se usar com qualquer que precisar "abrir, fechar, liberar" como conexão com base de dados, conexão de rede e muitos outros
'''