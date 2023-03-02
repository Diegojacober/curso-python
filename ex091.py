import random, time, operator
pessoas  = {'diego':0, 'kadu':0, 'nicole':0, 'angelo':0}

for k, v in pessoas.items():
    valor = random.randint(1,7)
    pessoas[k] = valor
    time.sleep(1)
    print(f'{k} tirou {valor}')

ranking = sorted(pessoas.items(), key=operator.itemgetter(1), reverse=True) 

print('{:=^50}'.format(' RANKING '))
for i, v in enumerate(ranking):
    time.sleep(1)
    print(f'{i+1}º Lugar: {v[0]} com {v[1]} ')

print('{:=^50}'.format('='))
