tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('FIM DO IF')

print('CARRO NOVO' if tempo <=3 else 'CARRO VELHO')
print('#'*20, 'FIM', '#'*20)

nome = input('Qual seu nome? ')
if nome.lower() == 'diego':
    print('Que nome lindo!!')
print('Prazer em te conhecer {}'.format(nome))
