idade = int(input('Digite a idade do atleta: '))

if idade <= 9:
    print('O atleta esta classificado como mirim')
elif idade <= 14:
    print('O atleta esta classificado como infantil')
elif idade <= 19:
    print('O atleta esta classificado como junior')
elif idade <= 25:
    print('O atleta esta classificado como sênior')
else:
    print('O atleta esta classificado como master')