salario = float(input('Qual o salário atual do funcionário? R$'))
a = 0.15 * salario
print('O salário do funcionário que era {:.2f}, com um aumento de 15%, agora passa a ser de R${:.2f}'.format(salario, (a+salario)))
