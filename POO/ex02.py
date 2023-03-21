"""
1 - Crie uma classe Carro (nome)
2 - Crie uma classe Motor (nome)
3 - Crie uma classe Fabricante (nome)
4 - Faça a ligação entre carro tem motor
Obs: Um motor pode ser ve varios carros
5 - Faça a ligação entre Carro e Fabricante
Obs: Um fabricante pode fabricar varios carros
Exiba o nome do carro, motor e fabricantes na tela
"""

class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._motor = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
        
class Motor:
    def __init__(self, nome) -> None:
        self.nome = nome
        
class Fabricante:
    def __init__(self, nome) -> None:
        self.nome = nome
        
fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')



fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.motor.nome, fusca.fabricante.nome)

uno = Carro('uno')
fiat = Fabricante('fiat')
motor_1_0 = Motor('1.0')

uno.fabricante = fiat
uno.motor = motor_1_0
print(uno.nome, uno.motor.nome, uno.fabricante.nome)
