somaIdade = 0
maiorIdadeHomens = 0
nomeVelho = ''
totMulheres = 0
for p in range(1, 5):
    print('----- {}º PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomens = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomens:
        maiorIdadeHomens = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulheres += 1
mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(maiorIdadeHomens, nomeVelho))
print('Existem {} mulheres com menos de 20 anos'.format(totMulheres))
