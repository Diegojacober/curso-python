# lista = [4,32,4,5,8,5,8,4,8,94,9,94,89,4]
# lista.sort() #ordena a lista
#sorted(lista) # cria uma lista rasa

lista = [
    {'nome': 'Diego', 'sobrenome': 'Alencar'},
    {'nome': 'Angelo', 'sobrenome': 'Carnevale'},
    {'nome': 'Nicole', 'sobrenome': 'Siqueira'},
    {'nome': 'Carlos', 'sobrenome': 'Barbosa'},
]
#ordenando um dicionario
def ordena(item):
    #ordena pelo nome
    return item['nome']
    #ordena pelo sobrenome
    # return item['sobrenome']

#lista.sort(key=ordena)

# com uma funcao lambda
lista.sort(key=lambda item: item['nome'])
lista2 = sorted(lista,key=lambda item: item['sobrenome'])

for item in lista:
    print(item)
    
print('='*50)
for item in lista2:
    print(item)
    
    
#lambda complexa

def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y

def criar_multiplicardor(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


print(executa(lambda x,y: x+y, 4,5))
