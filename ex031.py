viagem = float(input('Quantos km terá sua viagem? '))

if viagem <= 200.00:
    print('O preço da passagem por pessoa custará R${} por pessoa'.format(viagem * 0.50))
else:
    print('O preço da passagem por pessoa custará R${} por pessoa'.format(viagem * 0.45))