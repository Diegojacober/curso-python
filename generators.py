"""
Funções que pausam inves de finalizar a execução
"""

def generator(n=0):
    nome = input('Me diga seu nome: ')
    yield nome #Pausar
    sobrenome = input('Me diga seu sobrenome: ')
    yield sobrenome
    yield f'Olá {sobrenome}, {nome}'

gen = generator(n=0)
for n in gen:
    print(n)