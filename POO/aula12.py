"""
Composição é uma especialidade da agregação
Mas nela, quando o objeto "pai" for apagado, todas
as referências dos objetos filhos também são apagadas
"""
class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []
        
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua,numero))
        
    def listar_enderecos(self):
       for endereco in self.enderecos:
           print(endereco.rua, endereco.numero)
        
    #garbage collector do pyhton
    def __del__(self):
        print('#########APAGANDO', self.nome)
    
        
        
class Endereco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero = numero
        
    #garbage collector do pyhton
    def __del__(self):
        print('#########APAGANDO', self.rua, self.numero)
        
        
cliente1 = Cliente('Pedro')
cliente1.inserir_endereco('av Brasil', 1939)
cliente1.inserir_endereco('licheinsteiner', 45)

del(cliente1)
#assim da erro porque apaga o objeto e todas suas refernecias

cliente1.listar_enderecos()
#ao acabar o codigo ele executa as funções __del__ 