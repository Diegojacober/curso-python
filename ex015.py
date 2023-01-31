dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodou com o carro? '))
valor = (dias * 60) + (km * 0.15)
print('O carro alugado por {} dias, rodando {}km custou {:.2f}'.format(dias, km, valor))
