p = float(input('Qual o preço do produto? R$'))
d = 0.05 * p
print('O produto que custava R${:.2f} com um desconto de 5% custará agora R${:.2f}'.format(p, (p-d)))
