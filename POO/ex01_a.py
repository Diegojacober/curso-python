# Exercicio - Salve sua classe em JSON
# Salve os dados da sua classe em json
# e depois crie novamente as instâncias
# Faça em arquivos separados
import json
CAMINHO_ARQUIVO = './POO/ex01.json'

class Pessoa:
    
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
p1 = Pessoa('João', 45)
p2 = Pessoa('Miguel', 32)
p3 = Pessoa('Maria', 19)

bd = [vars(p1), vars(p2), vars(p3)]

if __name__ == '__main__':
    with open(CAMINHO_ARQUIVO,'a',encoding='utf8') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)