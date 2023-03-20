"""
Relações entre classes: associação, agregação e composição
Associação é um tipo de relação onde os objetos estão ligados dentro do sistema
Essa relação é a mais comum entre os objetos e tem subconjuntos como agregação e composição
Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto
A associação não espcifica como um objeto controla o ciclo de vida de outro objeto.
"""
class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None
        
    @property
    def ferramenta(self):
        return self._ferramenta
        
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta     
        
class FerramentaDeEscrever:
    def __init__(self, nome) -> None:
        self.nome = nome
        
    def escrever(self):
        return f'{self.nome} está escrevendo'
    
escritor = Escritor('Diego')
caneta = FerramentaDeEscrever('Caneta')
escritor.ferramenta = caneta

print(caneta.escrever())
print(escritor.ferramenta.escrever())

maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_de_escrever
print(escritor.ferramenta.escrever())
