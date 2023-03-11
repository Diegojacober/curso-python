def digite_int(msg):
    while True:
        n = input(msg).strip()
        try:
            n = int(n)
        except (ValueError,TypeError):
            print('\033[31mTipo inválido, digite um numero inteiro\033[m')
        else:
            return n
    
        
n = digite_int('Digite um número: ')

if n % 2 == 0:
    print(f'{n} número é par')
else:
    print(f'{n} número é impar')
    