n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
media = (n1+n2+n3+n4) / 4

if media <= 6.9:
    print('A média do aluno foi {}, ele está reprovado'.format(media))
elif 7 == media or media <= 7.5:
    print('A média do aluno foi {}, ele está de recuperação'.format(media))
else:
    print('A média do aluno foi {}, ele passou'.format(media))
