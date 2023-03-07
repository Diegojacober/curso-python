def ajuda():
    while True:
        msg = input('\033[30;42;7mDigite o que deseja saber:\033[m ')
        if msg.upper().strip() == 'FIM': 
            print('Obrigado pela preferência!!!')
            break
        else:
            print(f'\033[32;44;7{help(msg)}\033[m')
            
ajuda()