from random import randint
numeroUser = int(input('tente adivinhar o numero inteiro: '))
numeroAleatorio = randint(0, 10)
tentativas = 1
while numeroUser != numeroAleatorio:
    if numeroUser > numeroAleatorio:
     numeroUser = int(input('Menos..., tente novamente: '))
    if numeroUser < numeroAleatorio:
        numeroUser = int(input('Mais..., tente novamente: '))
    tentativas += 1
print('Você precisou de {} tentativas'.format(tentativas))