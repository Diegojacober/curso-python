import random

n = random.randint(1, 5)
chute = int(input('Pensei em um número entre 0 e 5, qual número você acha que é? '))
if n == chute:
    print('Acertou eu pensei em {} mesmo'.format(n))
else:
    print('Errou! eu pensei em {}'.format(n))
