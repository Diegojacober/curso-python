continuar = 's'
numeros = []

while continuar in 'Ss':
    n = int(input('Digite um número inteiro: '))
    if n not in numeros:
        numeros.append(n)
        print('Adicionando numero...')   
    else:
        print('Número ja adicionado')    
    continuar = input('Deseja continuar? [S/N] ').lower().strip()[0]

numeros.sort()
print(f'Você digitou os valores {numeros}')
