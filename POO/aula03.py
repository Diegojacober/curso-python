#Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False) -> None:
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        if self.filmando:
            return f'A camêra {self.nome} já está filmando'
        
        self.filmando = True
        return f'{self.nome} está filmando'
    
    def parar_filme(self):
        if not self.filmando:
            return f'A camera {self.nome} não está filmando'
        self.filmando = False
        return f'Parando filme da camara {self.nome}'
    
    def fotografar(self):
        if self.filmando:
            return f'Não é possivel fotografar enquanto a camera filma'
        return f'A {self.nome} está fotografando'
        
    
    
c1 = Camera('Canon')
print(c1.filmar())
print(c1.filmando)
print(c1.filmar())
print(c1.fotografar())
print(c1.parar_filme())
print(c1.filmando)
print(c1.fotografar())

c2 = Camera('Sony')
print(c2.filmando)