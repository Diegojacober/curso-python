from datetime import date
anoNasc = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - anoNasc
if idade == 18:
    print('Este é o seu ano de alistamento militar')
elif idade < 18:
    print('Você ainda está muito novo, só deverá se alistar em {}'.format(date.today().year + (18 - idade)))
else:
    print('Você ja deveria ter se alistado {} anos atrás em {}'.format(idade-18,date.today().year - (idade - 18))) 