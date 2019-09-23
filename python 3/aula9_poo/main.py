'''
Composição - Relação mais forte entre classes. Uma classe terá comando nos objetos de outra classe.
Caso a classe principal seja apagada, todos os objetos que ela usou serão apagados com ela.
'''

#nesse caso a classe Endereço pertence a classe Cliente

from classe import Cliente, Endereço

cliente1 = Cliente('Victor', 22)
cliente1.insere_endereço('Rio de Janeiro', 'RJ')
cliente1.insere_endereço('Santa Catarina', 'SC')
print(cliente1.nome)
cliente1.lista_endereços()
print()

cliente2 = Cliente('Luiz', 32)
cliente2.insere_endereço('Belo Horizonte', 'MG')
print(cliente2.nome)
cliente2.lista_endereços()
print()

cliente3 = Cliente('João', 35)
cliente3.insere_endereço('Salvador', 'BA')
print(cliente3.nome)
cliente3.lista_endereços()
print()

