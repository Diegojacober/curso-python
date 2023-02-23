matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totPares = 0
totTerceiraCol = 0
maiorSegundaLin = 0
for l in range(3):
    for c in range(3):
        n = int(input(f'Digite um valor para [{l}][{c}]: '))
        matriz[l][c] = n
        if n % 2 == 0:
            totPares += n
        if l == 1:
            if c == 0 or n > maiorSegundaLin:
                maiorSegundaLin = n
        if c == 2:
            totTerceiraCol += n
print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*30)
print(f'Total de soma dos numeros pares: {totPares}')
print(f'Total de soma dos numeros da terceira coluna: {totTerceiraCol}')
print(f'maior numero da segunda linha: {maiorSegundaLin}')