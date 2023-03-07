def ficha(nome='\033[33m<DESCONHECIDO>\033[m',gols=0):
    print(f'O jogador {nome} marcou {gols} gols na temporada')

print('-'*40)
n = input('Nome: ')
g = input('Gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)