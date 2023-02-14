import random
par = impar = jog = maq = 0

while True:
    jog = int(input('Quantos você quer jogar? '))
    jogOpcao = input('Par (P) ou Impar (I) ?').upper().strip()
    maq = random.randint(0, 10)
    if jogOpcao in 'Pp':
        if (jog + maq) % 2 == 0:
            print(f'Você ganhou, você jogou {jog} e a maquina {maq}')
        elif (jog + maq) % 2 != 0:
            print(f'Você perdeu, você jogou {jog} e a maquina {maq}')
            break
    if jogOpcao in 'Ii':
        if (jog + maq) % 2 == 0:
            print(f'Você perdeu, você jogou {jog} e a maquina {maq}')
            break
        elif (jog + maq) % 2 != 0:
            print(f'Você ganhou, você jogou {jog} e a maquina {maq}')
