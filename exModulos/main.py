import moeda


p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.moeda(valor=moeda.metade(p),moeda="R$")}')
print(f'O dobro de {p} é {moeda.moeda(valor=moeda.dobro(p),moeda="R$")}')
print(f'Aumentando 10% de {p}, teremos {moeda.moeda(valor=moeda.aumentar(p, 10),moeda="R$")}')
print(f'Diminuindo 10% de {p}, teremos {moeda.moeda(valor=moeda.diminuir(p, 10),moeda="$")}')
