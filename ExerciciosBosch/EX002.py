from random import randint
import datetime, pygame, time

def winMusic():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('ExerciciosBosch\musicavitoria.mp3')
    pygame.mixer.music.play(loops=0, start=12.0)
    pygame.event.wait()

def primeNumber():
    randNumber = 0
    isPrime = False
    while isPrime == False:
        randNumber = randint(0,1001)
        for count in range(2,randNumber - 1):
            if randNumber % count == 0 or randNumber % 5 == 0:
                break
            else:
                isPrime = True
    return randNumber

start_time = time.time()
randNumber = primeNumber()
userChance = 15
userLife = 1000
while True:
    
    userNumber = int(input('Tente adivinhar o número que eu estou pensando você tem 15 chances ou 1000 pontos de vida: '))
    
    while userNumber != randNumber:
        end_time = time.time()
        time_diff = end_time - start_time
        if time_diff <= 60:
            if userLife > 0 and userChance > 0:
                userChance = userChance - 1
                print(f'\033[33mVocê perdeu uma chance, agora tem {userChance} \033[m')
                if userNumber % 2 == 0:
                    userLife = userLife - abs(userNumber)
                    if userLife < 0: userLife = 0
                    print(f'\033[31mVocê perdeu {abs(userNumber)} pontos de vida, agora tem {userLife} \033[m')
                    if userNumber < randNumber:
                        userNumber = int(input('Um pouco mais. Tente novamente: '))
                    elif userNumber > randNumber:
                        userNumber = int(input('Um pouco menos. Tente novamente: '))
                else:
                    if userNumber < randNumber:
                        userNumber = int(input('Um pouco mais. Tente novamente: '))
                    elif userNumber > randNumber:
                        userNumber = int(input('Um pouco menos. Tente novamente: '))
                        
            else:
                print(f'\033[31mSuas tentativas acabaram ☹  -- o número correto era {randNumber} \033[m')
                print(datetime.datetime.now().microsecond)
                break
        else:
            print(f'\033[31mSeu tempo acabou ☹  -- o número correto era {randNumber} \033[m')
            print(datetime.datetime.now().microsecond)
            break
    
    if userNumber == randNumber:
        print('🎉'*31)
        print('{:🎉^50}'.format('\033[32mParabéns você acertou!!! \033m'))
        print('🎉'*31)
        winMusic()
        break
   
    
    
    
    
    
    

