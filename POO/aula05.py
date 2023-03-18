#__dict__ e vars para atributos de instância
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
# p1.nome = 'Outro nome que eu mudei'
# p1.__dict__['outra'] = ['coisa'] # não é comum mas existe e também é editável
print(p1.__dict__)
# o vars chama o dict
print(vars(p1))

dados = {'nome': 'Diego', 'idade': 18}
p2 = Pessoa(**dados)
print(vars(p2))
