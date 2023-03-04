from time import sleep
jogador = {}
jogadores = []
while True:
    jogador['nome'] = input('Nome do jogador: ')
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    total = 0

    for partida in range(jogador['partidas']):
        gols = int(input(f'Quantos gols {jogador["nome"]} fez na partida {partida + 1}:  '))
        jogador['gols'].append(gols)
    for i in range(jogador['partidas']): print(f'\t=> partida {i+1} -', jogador['gols'][i], ' Gols')
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    jogador.clear()
    while True:
         cnt = input('Deseja continuar: [S/N]: ').upper()[0].strip()
         if cnt in 'SN':
            break
         print('ERRO! Digite apenas S ou N ')
    if cnt == 'N': break

print('-='*50)
print('Nome\tPartidas\t\t Gols \t\t\t Total de Gols\n')
for j in jogadores:
    print(f'{j["nome"]} \t {j["partidas"]} \t\t\t {j["gols"]} \t {j["total"]}')
print('-='*50)
while True:
    busca = int(input('Qual jogador você deseja ver o código? '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador no indice {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}')
        sleep(1)
        print(f'\t {jogadores[busca]["partidas"]} jogos - Gols por partida: {jogadores[busca]["gols"]}, total de {jogadores[busca]["total"]} gols')