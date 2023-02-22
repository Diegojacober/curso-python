lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = input('Deseja continuar? ').lower().strip()[0]
    if resp not in 'Ss':
        break
print(f'Quantidade de números digitados: {len(lista)}')
lista.sort(reverse = True)
print(f'Lista ordenada de forma descrescente: {lista}')

# ou if 5 in lista:
if lista.count(5) > 0:
    print('O número 5 foi encontrado na lista')
else:
    print('O número 5 não está na lista')
