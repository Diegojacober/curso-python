s = 0
for c in range(1, 8):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        s += n
print('A soma dos números pares é {}'.format(s))
