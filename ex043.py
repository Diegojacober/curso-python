from math import pow
peso = float(input('Qual seu peso? (Kg)  '))
altura = float(input('Qual sua altura? (M)  '))
imc = peso / pow(altura,2)

if imc <= 18.5:
    print('seu imc é de {:.2f}, \033[31mVocê está abaixo do peso \033[m'.format(imc))
elif imc <= 25:
    print('seu imc é de {:.2f}, \033[1;32mVocê está no peso ideal \033[m'.format(imc))
elif imc <= 30:
    print('seu imc é de {:.2f}, \033[1;33mVocê está com sobrepeso \033[m'.format(imc))
elif imc <= 40:
    print('seu imc é de {:.2f}, \033[1;31mVocê está com obesidade \033[m'.format(imc))
else:
    print('seu imc é de {:.2f}, \033[1;30;41mVocê está com obesidade mórbida \033[m'.format(imc))
    