from random import randint

def primeNumber():
    randNumber = 0
    isPrime = False
    while isPrime == False:
        randNumber = randint(0,1001)
        for count in range(2,randNumber - 1):
            if randNumber % count == 0:
                break
            else:
                isPrime = True
    return randNumber


randNumber = primeNumber()
userChance = 15
userLife = 1000
print(randNumber)
while True:
    
    userNumber = int(input('Tente adivinhar o número que eu estou pensando você tem 15 chances ou 1000 pontos de vida: '))
    
    
    while userNumber != randNumber:
        if userLife > 0 and userChance > 0:
            if userNumber % 2 == 0:
                userLife = userLife - abs(userNumber)
                print(f'\033[31mVocê perdeu {abs(userNumber)} pontos de vida, agora tem {userLife} \033[m')
                if userNumber < randNumber:
                    userChance = userChance - 1
                    print(f'Você perdeu uma chance, agora tem {userChance}')
                    userNumber = int(input('Um pouco mais. Tente novamente: '))
                elif userNumber > randNumber:
                    userChance = userChance - 1
                    print(f'Você perdeu uma chance, agora tem {userChance}')
                    userNumber = int(input('Um pouco menos. Tente novamente: '))
            else:
                if userNumber < randNumber:
                    userChance = userChance - 1
                    print(f'Você perdeu uma chance, agora tem {userChance}')
                    userNumber = int(input('Um pouco mais. Tente novamente: '))
                elif userNumber > randNumber:
                    userChance = userChance - 1
                    print(f'Você perdeu uma chance, agora tem {userChance}')
                    userNumber = int(input('Um pouco menos. Tente novamente: '))
                    
        else:
            print(f'Suas tentativas acabaram ☹  -- o número correto era {randNumber}')
            break
    
    if userNumber == randNumber:
        print('Parabéns você acertou')
        break
   
    
    
    
    
    
    

