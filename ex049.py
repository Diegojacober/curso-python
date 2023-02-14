n = int(input('Digite o número qual deseja ver a tabuada: '))

print('='*20)
print('Tabuada do {}'.format(n))
print('=' * 20)
for c in range(11):
    print(' {} x {} = {}'.format(c, n, c*n))