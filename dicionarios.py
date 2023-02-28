dados = {} # or dados = dict()
dados = {'nome': 'Diego', 'sexo': 'M', 'idade': 18}
print(f"O {dados['nome']} tem {dados['idade']}")

print(dados.keys())
print(dados.values())
print(dados.items())

# for d, v in dados.keys():
#     print(d)
del dados['sexo']
dados['idade'] = 980
dados['peso'] = 69.6
for i, v in dados.items():
    print(f'{i} = {v}')

brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]['uf'])

for i,v in enumerate(brasil):
    print(f"{brasil[i]['uf']} - {brasil[i]['sigla']}")

estados = {}
brasil = []

for c in range(3):
    estados['uf'] = input('Unidade federativa: ')
    estados['sigla'] = input('Sigla do estado: ')
    brasil.append(estados.copy())
for e in brasil:
    print(e)
    for v in e.values():
        print(v, end=' ')
    print()
    for k in e.keys():
        print(k, end=' ')
