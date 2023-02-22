#listas compostas
pessoas = [['Diego', 18], ['Janete', 40], ['Bianca', 11]]

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos')


galera = []
dados = []
for c in range(3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')