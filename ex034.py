salario = float(input('Digite o salário do funcionário: '))

if salario < 1250.00:
    print('O novo salário é de R${:.2f}'.format(salario + (salario * 0.15)))
if salario > 1250.00:
    print('O novo salário é de R${:.2f}'.format(salario + (salario * 0.10)))
    