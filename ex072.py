cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito',
        'nova', 'dez', 'onze', 'doze',
        'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')

continuar = 's'
while continuar in 'Ss':
    n = int(input('Digite um numero entre 0 e 20: '))

    if n <= 20 and n >= 0:
        print(f'Você digitou o número {cont[n]}')
        continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
        if continuar in 'Nn': break
    print('Digite novamente: ',end='')