"""
super() é a superClasse na sub-classe
"""
# class Pessoa:
#     def __init__(self, nome, sobrenome) -> None:
#         self.nome = nome
#         self.sobrenome = sobrenome
    
# class Cliente(Pessoa):
#     ...
    
# class Fornecedor(Pessoa):
#     ...

# c1 = Cliente('Diego', 'Alencar')
# f1 = Fornecedor('Diego', 'Jacober')

class A:
    atributo_a = 'valor A'
    def metodo(self):
        print('A')
        
class B(A):
    atributo_b = 'valor B'
    def metodo(self):
        print('B')
        
class C(B):
    atributo_c = 'valor C'
    def metodo(self):
        # super(B,self).metodo()
        super().metodo()
        print('C')
        
C = C()
print(C.atributo_a)
print(C.atributo_b)
print(C.atributo_c)
C.metodo()