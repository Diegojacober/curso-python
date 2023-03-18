"""
@staticmethod (métodos estáticos)
Métodos estáticos são metodos que estão dentro da classe, mas não tem acesso ao self nem ao cls
ou seja, são funções que existem dentro da sua classe
"""

class Classe:
    @staticmethod
    def static_function(*args, **kwargs):
        print('oi', args, kwargs)
        
        
c1 = Classe()
c1.static_function(1, 2, 3, 4, 5, 6)
#ou
Classe.static_function(11, 12, 13)