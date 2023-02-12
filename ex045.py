import random
jogadaUser = int(input(
    'Suas opções: \n[ 0 ] Pedra \n[ 1 ] Papel \n[ 2 ] Tesoura \n Qual sua jogada? '))
jogadaComputer = random.randint(0, 2)
itens = ['Pedra', 'Papel', 'Tesoura']

if jogadaUser > 3:
    print('\033[4;31mJogada inválida\033[m')
else:
    if jogadaComputer == 0:
        if jogadaUser == 0:
            print('O computador escolheu {}, \033[1;33mempate\033[m'.format(itens[jogadaComputer]))
        elif jogadaUser == 1:
            print('O computador escolheu {}, \033[1;32mvocê venceu\033[m'.format(itens[jogadaComputer]))
        elif jogadaUser == 2:
            print('O computador escolheu {}, \033[1;31mvocê perdeu\033[m'.format(itens[jogadaComputer]))
    elif jogadaComputer == 1:
        if jogadaUser == 0:
            print('O computador escolheu {}, \033[1;31mvocê perdeu\033[m'.format(itens[jogadaComputer]))
        elif jogadaUser == 1:
            print('O computador escolheu {}, \033[1;33mempate\033[m'.format(itens[jogadaComputer]))
        elif jogadaUser == 2:
            print('O computador escolheu {}, \033[1;32mvocê venceu\033[m'.format(itens[jogadaComputer]))
    elif jogadaComputer == 2:
        if jogadaUser == 0:
            print('O computador escolheu {}, \033[1;32mvocê venceu\033[m'.format(itens[jogadaComputer]))
        elif jogadaUser == 1:
            print('O computador escolheu {}, \033[1;31mvocê perdeu\033[m'.format(itens[jogadaComputer]))
        elif jogadaUser == 2:
            print('O computador escolheu {}, \033[1;33mempate\033[m'.format(itens[jogadaComputer]))

