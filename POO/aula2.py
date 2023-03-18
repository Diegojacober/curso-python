# Metodos em instâncias de classes

class Carro:
    def __init__(self,nome='Carro sem nome') -> None:
        # self.nome = 'Fusca' #Hard coded
        self.nome = nome
        
    #todo metodo recebe como primeiro parametro o self
    def acelerar(self):
        return f'Acelerando o {self.nome}'
    
fusca = Carro('Fusca')
print(fusca.nome)
print(fusca.acelerar())

celta = Carro(nome='Celta')
print(celta.nome)
print(celta.acelerar())
