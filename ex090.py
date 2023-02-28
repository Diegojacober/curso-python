pessoa = {}
pessoa['nome'] = input('Digite o nome: ')
pessoa['media'] = input('Digite a média: ')

if int(pessoa['media']) < 5:
    pessoa['situacao'] = 'reprovado'
elif int(pessoa['media']) >= 5 and int(pessoa['media']) <= 6:
    pessoa['situacao'] = 'recuperação'
else:
    pessoa['situacao'] = 'aprovado'
print('-=' * 50)
for k, v in pessoa.items():
    print(f'\t  {k} = {v}')
