times = ('Corinthians', 'Santos', 'Flamengo', 'Vasco', 'Coritiba', 'Internacional', 'Grêmio',
         'Atlético-MG', 'Atlethico-PR', 'Cruzeiro', 'Juventude', 'América-MG', 'Cuiaba',
         'Chapecoense', 'Fluminense', 'Goiás', 'São Paulo', 'Fortaleza', 'Bragantino', 'Palmeiras')

print(f'\033[32mO G4 do Brasileirão do Diego é: \n 1º {times[0]} \n 2º {times[1]} \n 3º {times[2]} \n 4º {times[3]} \033[m')
print(f'\033[31mOs ultimos 4 colocados são: \n 17º {times[16]} \n 18º {times[17]} \n 19º {times[18]} \n 20º {times[19]} \033[m')
print(f'Os times em ordem alfabética ficam: {sorted(times)}')
print('='*100)
posicao = int(input('\n Digite a posição qual deseja saber o time: '))
if posicao > 0 and posicao <= 20:
    print(f'O time que esta na {posicao}º posição é o {times[posicao-1]}')
else:
    print('Posição inválida')