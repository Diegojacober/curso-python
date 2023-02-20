lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita', 'Amora')

for cont in range(0,len(lanche)):
    print(f'Comida {lanche[cont]} ')

print('\033[31m=\033[m'*50)

for comida in lanche:
    print(f'Comida: {comida}')
    
print('\033[34m=\033[m'*50)
    
for pos,comida in enumerate(lanche):
    print(f'Comida: {comida} - posição {pos}')

print('\033[32m=\033[m'*50)

# ordem alfabética
print(sorted(lanche))

a = (2,5,4)
b = (5, 8, 1, 2)
c = a + b
# junta as tuplas
print(c)
# conta quantas vezes aparece o numero 5
print(c.count(5))
# mostra a posição do elemento, sempre a primeira ocorrendia
print(c.index(2))
# a partir de uma determinada posição elemento,posição
print(c.index(2,5))

print('\033[33m=\033[m'*50)
pessoa = ('Diego', 18, 'M', 69.6)
print(pessoa)
#só da para apagar a tupla inteira
del(pessoa)