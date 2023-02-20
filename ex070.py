total = totmil = menor = cont = 0
barato = ''
while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {totmil} produtos com preços maiores do que R$ 1000,00')
print(f'O produto mais barato custa R${menor:.2f} ({barato})')