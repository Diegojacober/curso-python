from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10),
           randint(1,10), randint(1,10), randint(1,10), randint(1,10),
           randint(1,10), randint(1,10))

for numero in numeros:
    print(numero,end=' ')
    
print(f'\n O menor numero sorteado foi {min(numeros)}')
print(f'\n O maior numero sorteado foi {max(numeros)}')