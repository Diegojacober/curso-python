palavras = ('Diego','Alencar','Jacober','Python',
            'Ryzen','PHP','tupla','palavras',
            'curso','inteligencia','artificial','youtube')

print('-'*30)
print('{:^30}'.format('Vogais de cada palavra'))
print('-'*30)
for palavra in palavras:
    print('\n',palavra,end=': ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
