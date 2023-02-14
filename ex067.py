n = 0
while True:
    n = int(input('Digite o numero o qual deseja ver a tabuada: '))
    if n > 0:
        for x in range(11):
            print(f'{n} x {x} = {n * x}')
    else:
        break