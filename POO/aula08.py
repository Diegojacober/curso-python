"""
@property - um getter no modo pythôonico
getter - um metodo para obter um atributo
@setter - é necessário ter uma @property para escrever o @setter

modo pythônico - modo do python de fazer as coisas
@porperty é uma prorpriedade do objeto, ela é um
método que se comporta como um atributo
Geralmente é usada nas seguintes situações:
- como getter
- para evitar quebrar código cliente
- para habilitar setter
- para executar ações ao obter um atributo
"""

class Caneta:
    def __init__(self, cor, marca) -> None:
        # self._cor = cor
        self.cor = cor # assim executa o setter no inicio
        self.marca = marca
    
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, value):
        if value == 'verde':
            raise ValueError('Não aceito a cor verde')
        self._cor = value
        
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, value):
        self._marca = value
        
        
#ATRIBUTO COM UNDERLINE _cor -> protected, é protegido da classe. Não devem ser usados fora da classe

####### CODIGO CLIENTE É O CODIGO QUE USA A SUA CLASSE
caneta = Caneta('Azul', 'Bic')


#para o codigo cliente é um atributo, mas na classe é um metodo
print(caneta.cor)
caneta.cor = 'preta'
print(caneta.cor)

print(caneta.marca)
caneta.marca = 'Tilibra'
print(caneta.marca)