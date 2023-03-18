#Métodos de classe + factories
# São métodos onde o self será cls, ou seja,
# ao invés de receber a instancia no primeiro parâmetro,
# receberemos a própria classe
import datetime
class Pessoa:
    ano = datetime.datetime.today().year # atributo de classe
    
    def __init__(self, nome, idade, divida) -> None:
        self.nome = nome 
        self.idade = idade
        self.divida = divida
        
    @classmethod    
    def metodo_de_classe(cls):
        ...
        
    @classmethod  # aqui tem uma factorie
    def zerar_dividas_e_18_anos(cls,nome):
        # criando um objeto
        return cls(nome,18,0)
    
p1 = Pessoa('Marcos', 26, 5000)
print(vars(p1))

nomes = ['angelo','cadu','nicole','diego']
pessoas = []

for chave,nome in enumerate(nomes):
    p = Pessoa.zerar_dividas_e_18_anos(nome)
    pessoas.append(vars(p))
    
print('\n\n',pessoas) 
    