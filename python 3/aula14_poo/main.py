'''
Criando exceções em POO
'''

#para criar sua exceção personalizada em POO, basta apeas fazer o seguinte:
class TaErradoError(Exception):
    pass

#tratando exceção
def testar():
    raise TaErradoError('Errado!')

try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')