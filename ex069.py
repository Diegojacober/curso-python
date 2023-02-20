
mais18 = 0
homens = 0
mulheres = 0
cnt = 'S'

while cnt in 'Ss':
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    if idade > 18:
        mais18 += 1
        if sexo in 'Mm':
            homens += 1
        if idade < 20 and sexo in 'Ff':
            mulheres += 1
    if idade < 20 and sexo in 'Ff':
        mulheres += 1
    if sexo in 'Mm':
        homens += 1
    cnt = input('Deseja continuar [S/N]? ')

print('Mulheres com menos de 20 anos: ',mulheres)
print('Homens: ',homens)
print('Quantidade de pessoas com mais de 18 anos: ',mais18)