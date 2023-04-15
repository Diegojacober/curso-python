"""
Funções que pausam inves de finalizar a execução
"""

# def generator(n=0):
#     yield 1 # retorna aqui e para ate chegar um next
#     print('Continuando...')
#     yield 2
#     print('Continuando ainda')
#     yield 3
#     print('A função vai acabar')

# gen = generator(n=0)
# print(next(gen))
# print(next(gen))

# for n in gen:
#     print(n)


# def generator(n=0, maximum=10):
#     while True:
#         yield n
#         n += 1
#         if n > maximum:
#             return
        
# gen = generator(maximum=500)
# for n in gen:
#     print(n)


########Yield from########

# def gen1():
#     yield 1
#     yield 2
#     yield 3
    
# def gen2(gen):
#     yield from gen()
#     yield 4
#     yield 5
#     yield 6
    
# def gen3():
#     yield 10
#     yield 20
#     yield 30
    

# g = gen2(gen3)
# for n in g:
#     print(n)


# def generator(n=0):
#     nome = input('Me diga seu nome: ')
#     yield nome #Pausar
#     sobrenome = input('Me diga seu sobrenome: ')
#     yield sobrenome
#     yield f'Olá {sobrenome}, {nome}'

# gen = generator(n=0)
# for n in gen:
#     print(n)
    
    
def nome():
    nome = input('Digite seu nome: ')
    yield nome
    sobrenome = input('Digite seu sobrenome: ')
    yield sobrenome
    return

nomeUser = nome()

if next(nomeUser).strip() == 'Diego':
    sobrenome = next(nomeUser)
    print('Diego',sobrenome)
else:
    print('Acabou não é o Diego')