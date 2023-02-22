numeros = [[],[]]
for i in range(7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

numeros[0].sort()
numeros[1].sort()
print(f'Números pares: {numeros[0]}')
print(f'Números impares: {numeros[1]}')