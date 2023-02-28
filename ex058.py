from random import randint
numeroUser = int(input('tente adivinhar o numero inteiro: '))
numeroAleatorio = randint(0, 100)
tentativas = 1

mult = 0

while True:
    for count in range(2, numeroAleatorio):
        if numeroAleatorio % count == 0:
            mult += 1
            numeroAleatorio = randint(0, 100)
        mult = 0
        
    if mult == 0:
        while numeroUser != numeroAleatorio:
            if numeroUser > numeroAleatorio:
                numeroUser = int(input('Menos..., tente novamente: '))
            if numeroUser < numeroAleatorio:
                numeroUser = int(input('Mais..., tente novamente: '))
            tentativas += 1
        print(f'Você precisou de {tentativas} tentativas')
        break
