from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Victor')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

#imprimindo de forma independente
print(escritor.nome)
print(caneta.marca)
maquina.escrever()

#fazendo associação de classes enviando toda a classe (caneta) para o atributo em questão (ferramenta)
escritor.ferramenta = caneta
escritor.ferramenta.escrever()