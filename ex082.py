numeros = []
impares = []
pares = list()
resp = 's'

while resp in 'Ss':
    n = int(input('Digite um número inteiro: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = input('Deseja continuar? [S/N] ').lower().strip()

numeros.sort()
pares.sort()
impares.sort()
print(f'A lista completa é {numeros}')
print(f'A lista somente de números pares é {pares}')
print(f'A lista somente de números impares é {impares}')