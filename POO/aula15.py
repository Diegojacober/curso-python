"""
Herança multipla - Python Orientado a objetos
Uma classe pode estender varias outras classes.
Herança multipla e mixins
Log -> FileLog
Cliente(Pessoas, FileLog)
"""

class A:
    ...
    
    def quem_sou(self):
        print('A')
        
        
class B:
    ...
    
    def quem_sou(self):
        print('B')
        
        
class C:
    ...
    
    def quem_sou(self):
        print('C')
        

class D(B, C):
    ...
    
    def quem_sou(self):
        print('D')
        
d = D()

d.quem_sou()