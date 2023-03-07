from random import randint

def sorteia():
    numeros = []
    for i in range(5):
        numero = randint(0,101)
        numeros.append(numero)
    return numeros

def somaPar(lst):
    total = 0
    for n in lst:
        if n % 2 == 0:
            total += int(n)
    return total

numeros = sorteia()
print(f'Números sorteados: {numeros}')
print(f'Soma dos números pares: {somaPar(numeros)}')
