pt = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * rz
while pt <= decimo + rz:
    print('{} '.format(pt), end=' -> ')
    pt += rz
print('Fim')