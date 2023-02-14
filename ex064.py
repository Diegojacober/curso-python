n = int(input('Digite um número [ 999 para sair ]: '))
total = resultado = 0
while n != 999:
    total += 1
    resultado += n
    n = int(input('Digite um número [ 999 para sair ]: '))
print('Você digitou {} valores \nA soma entre eles é {}'.format(total,resultado))