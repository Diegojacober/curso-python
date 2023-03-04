import datetime
pessoa = {}

nome = input('Nome: ')
carteira_trabalho = int(input('Carteira de trabalho, caso não tenha digite 0: '))

if carteira_trabalho == 0:
    print(f'É necessário que {nome} faça sua carteira de trabalho, para continuar')
    exit()
else:
    ano_de_nasc = int(input('ano de nascimento: '))
    ano_carteira = int(input('Ano de contratação: '))
    idade = ano_carteira - ano_de_nasc;
    if idade < 15:
        print(f'{nome} não pode ser contratado(a) com {idade} anos')
        exit()
    salario = float(input('Salário: R$'))
    pessoa['nome'] = nome
    pessoa['ctps'] = carteira_trabalho
    pessoa['idade'] = idade
    pessoa['ano_de_nasc'] = ano_de_nasc
    pessoa['ano_carteira'] = ano_carteira
    pessoa['salario'] = salario
    pessoa['idade_aposentadoria'] = (datetime.datetime.now().year - ano_de_nasc) + ((pessoa['ano_carteira'] + 35) - datetime.datetime.now().year)

print('-=' * 30)
for k,v in pessoa.items():
    print(f'- {k} tem o valor de {v}')
    