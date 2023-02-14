pt = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * rz
for c in range(pt, decimo + rz, rz):
    print('{} '.format(c), end=' -> ')
print(' Fim')
