from datetime import date
atual = date.today().year
for pess in range(8):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        print('\033[1;32mEssa pessoa é maior de idade\033[m')
    else:
        print('\033[1;31mEsaa pessoa é de menor\033[m')
