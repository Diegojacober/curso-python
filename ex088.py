import random

print('-'*25)
print('{:^25}'.format('Jogos da mega sena'))
print('-'*25)

qntdJogos = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []
lista = []

for j in range(qntdJogos):
    for i in range(6):
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

print('{:^25}'.format('Os números sorteados foram: '))
for c, j in enumerate(jogos):
    print(f"{j}")
