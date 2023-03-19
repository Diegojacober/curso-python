#ENCAPSULAMENTO (Modificadores de acesso: public, protected, private)
"""
---> Python não tem modificadores de acesso, mas podem ser simuladas
Seguindo as conveções
    (sem underline) = public
        pode ser usado em qualquer lugar
    (um underline) = protected
        não deve ser usado fora das classes,
        somente na propria classe ou suas subclasses
    (dois underline) = private
        "name mangling" (desfiguração de nomes) em Python
        Só deve ser usado na classe em que foi declarado
"""

class Foo:
    def __init__(self) -> None:
        self.public = 'Isto é um atributo public'
        self._protected = 'Isto é um atributo protected'
        self.__private = 'Isto é um atributo private'
        
    def metodo_public(self):
        return 'metodo publico'
    
    def _metodo_protected(self):
        return 'metodo protected'
    
    def __metodo_private(self):
        return 'metodo private'