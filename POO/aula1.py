"""
Class - Classes são moldes para criar novos objetos as classes
geram novos objetos (instancias) que podem ter seus próprios atributos e métodos.
Os objetyos gerados pela classe podem usar seus dados internos para realizar varia açoões.
Padrão: PascalCase

"""

# string = 'Diego' # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
    
p1 = Pessoa('Diego', 'Alencar Jacober')

print(p1.nome)