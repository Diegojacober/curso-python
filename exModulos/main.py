import moeda


p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p,format=True)}')
print(f'O dobro de {p} é {moeda.dobro(p,format=True,formatacao="U$")}')
print(f'Aumentando 10% de {p}, teremos {moeda.aumentar(p, 10,True,"R$")}')
print(f'Diminuindo 10% de {p}, teremos {moeda.diminuir(valor=p, porcentagem=10,format=True,formatacao="$")}')
