"""
Herança Simples - Relações entre classes.
Assosiação (Usa), Agregação(tem), Composição (é dono de), Herança (É um)

Herança vs Composição

Classe principal (Pessoa)
    -> Super class, base class, parent class
Classes filhas (Cliente)
    -> sub class, child class, derived class   
"""
# para herdar: class ClasseFilha(SuperClass):
class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
    
class Cliente(Pessoa):
    ...
    
class Fornecedor(Pessoa):
    ...

c1 = Cliente('Diego', 'Alencar')
f1 = Fornecedor('Diego', 'Jacober')