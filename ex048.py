n = int(input('Digite um número: '))
s = 0
for c in range(1,n,2):
    if c % 3 == 0:
        print(c, end=" - ")
        s += c
print('\n A soma de todos os numeros é {}'.format(s))