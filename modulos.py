# import biblioteca ==> importar tudo que tem na biblioteca
# from biblioteca import livro ==> importa algo especifico de uma biblioteca
import math
import random
import emoji
num = int(input('Digite um número: '))

#arredonda pra cima
math.ceil(5.2)
#arredonda pra baixo
math.floor(5.9)
#elimina da virgula pra frente
math.trunc(5.2984941)
#potencia
math.pow(7,8)
#raiz quadrada
print('Raiz Quadrada de {} = {}'.format(num, math.ceil(math.sqrt(num))))
#fatorial !x
print('O fatorial de {} é {}'.format(num, math.factorial(num)))

print(f'Número aleatório: {random.random()}')
print(f'Número aleatório inteiro: {random.randint(1,5)}')
print(emoji.emojize('Python is :thumbsup:', language='alias'))

