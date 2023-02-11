n1 = float(input('Digite o número 1: '))
n2 = float(input('Digite o número 2: '))
if n1 > n2:
    print('O {:.2f} é maior que o {:.2f}'.format(n1,n2))
elif n2 > n1:
    print('O {:.2f} é maior que o {:.2f}'.format(n2,n1))
else:
    print('Os dois números são iguais')