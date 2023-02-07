velocidade = float(input('Qual a velocidade do carro em KM/H? '))

if velocidade > 80:
    excedente = velocidade - 80.00
    print('Você ultrapassou o limite de velocidade que é 80.00 Km/h, você deverá pagar uma multa de R${:.2f}'.format(excedente * 7))
else:
    print('Tenha um ótimo dia, continue dirigindo com responsabilidade')