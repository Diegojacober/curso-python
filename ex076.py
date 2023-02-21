produtos = ('Caderno', 14.50,
            'Caneta', 3.50,
            'Lápis', 1.20,
            'Borracha', 2.50,
            'Estojo', 8.00,
            'Mochila', 150.00)
print('-'*30)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-'*30)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'\033[34m{produtos[pos]:.<30}\033[m', end='')
    else:
        print(f'\033[32mR$ {produtos[pos]:>7.2f}\033[m')

