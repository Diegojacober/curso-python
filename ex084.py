pessoas = []
dados = []
maiorPeso = 0
menorPeso = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]
    pessoas.append(dados[:])    
    dados.clear()
    resp = input('Deseja continuar? [S/N] ').lower().strip()[0]
    if resp not in 'Ss':
        break

print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')

print(f'O menor peso registrado foi de {menorPeso:.2f} Kg, que pertecem a: ',end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(p[0],end=', ')
        
print(f'\nO maior peso registrado foi de {maiorPeso:.2f} Kg ', end= '')
for p in pessoas:
    if p[1] == maiorPeso:
        print(p[0],end=', ')

    