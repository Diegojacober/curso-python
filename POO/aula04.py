#Atributos da classe
import datetime
class Pessoa:
    ano_atual = datetime.datetime.now().year
    
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
    def get_ano_de_nascimento(self):
        # return self.ano_atual - self.idade
        return Pessoa.ano_atual - self.idade
    
    
p1 = Pessoa('João', 23)
p2 = Pessoa('Paulo', 41)
print(p1.get_ano_de_nascimento())
print(p2.get_ano_de_nascimento())