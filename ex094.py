pessoas = list()
pessoa = dict()
media = 0
while True:   
    pessoa['nome'] = input('Nome: ')
    while True:
         sexo = input('Sexo: [M/F]: ').upper()[0].strip()
         if sexo in 'MF':
            pessoa['sexo'] = sexo
            break
         print('ERRO! Digite apenas F ou M ')
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    cnt = 's'
    while True:
         cnt = input('Deseja continuar: [S/N]: ').upper()[0].strip()
         if cnt in 'SN':
            break
         print('ERRO! Digite apenas S ou N ')
    if cnt == 'N': break
print('-='*30)

print(f'A) Pessoas cadastradas {len(pessoas)}')

for i, v in enumerate(pessoas): media += pessoas[i]['idade']
print(f'B) Média de idade = {media/len(pessoas):.2f}')

print('C) Mulheres: ',end='')
for i, v in enumerate(pessoas):
    if pessoas[i]['sexo'] == 'F': print(f'{pessoas[i]["nome"]}',end='; ')
        
print('\nD) Pessoas com idade acima da média: ',end='')
for i, v in enumerate(pessoas):
    if pessoas[i]['idade'] > (media/len(pessoas)): print(f'{pessoas[i]["nome"]}, {pessoas[i]["idade"]} anos',end='; ')
