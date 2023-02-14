num = int(input('Digite um numero inteiro e descubra seu fatorial: '))


resultado = 1
count = num
print('Calculando {}! = '.format(num), end='')
while count > 0:
    print('{}'.format(count),end='')
    print(' x ' if count > 1 else ' = ', end='')
    resultado *= count
    count -= 1
    
print(resultado)