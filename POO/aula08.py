"""
@property - um getter no modo pythôonico
getter - um metodo para obter um atributo

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
    def __init__(self, cor) -> None:
        self.cor_tinta = cor
    
    @property
    def cor(self):
        return self.cor_tinta
    
    @property
    def marca(self):
        return 'Bic'
        
####### CODIGO CLIENTE É O CODIGO QUE USA A SUA CLASSE
caneta = Caneta('Azul')


#para o codigo cliente é um atributo, mas na classe é um metodo
print(caneta.cor)

print(caneta.cor_tinta)
print(caneta.marca)