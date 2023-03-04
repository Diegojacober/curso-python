jogador = {}
nome = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {nome} jogou? '))
jogador['nome'] = nome
jogador['partidas'] = partidas
jogador['gols'] = []
total = 0

for partida in range(partidas):
    gols = int(input(f'Quantos gols {nome} fez na partida {partida + 1}:  '))
    jogador['gols'].append(gols)
    total += gols

print('-='*50)
print(f'{jogador}')
print('-='*50)
for k,v in jogador.items(): print(f'- O campo {k} tem o valor de {v}')
print('-='*50)

print(f'O jogador {nome} jogou {partidas} partidas: ')

for i in range(jogador['partidas']): print(f'\t=> partida {i+1} -', jogador['gols'][i], ' Gols')

print(f'{jogador["nome"]} fez {total} gols em {jogador["partidas"]} partidas')
