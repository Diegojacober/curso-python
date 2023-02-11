salario = float(input('Qual seu salário? R$'))
valorImovel = float(input('Qual o valor do imóvel? R$'))
anos = int(input('QUantos anos de financiamento? '))
parcela = valorImovel / (anos * 12)
minimo = salario * 0.30
print(f'Para pagar uma casa de R${valorImovel:.2f} em {anos}, cada parcela sairá por R${parcela:.2f}')

if parcela <= minimo:
    print('Empréstimo concedido')
else:
    print('Empréstimo negado')