# Modularização -> surgiu na decada de 60 devido ao aumento dos sistemas industrais e comerciais,
# busca dividir um programa grande, aumentar a legibilidade e facilitar a manutenção
from modulos import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')