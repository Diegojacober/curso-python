# letra vermelha
print('\033[31mOlá, mundo')
# letra vermelha e fundo amarelo
print('\033[31;43mOlá, mundo')
# negrito, letra vermelha e fundo amarelo
print('\033[1;31;43mOlá, mundo')
# negrito, letra vermelha e fundo amarelo e finalizar formatação
print('\033[1;31;43mOlá, mundo\033[m')


print('\033[0;32;41mOlá, mundo\033[m')
print('\033[7;32;41mOlá, mundo\033[m')

print('Os valores são \033[0;32;47m{}\033[m e \033[36m{}\033[m'.format(4, 5))

print('Olá muito prazer em te conhecer {}{}{}'.format(
    '\033[4;34m', 'Diego', '\033[m'))

cores = {'limpa': '\033[m', 'azul': '\033[34m', 'pretoEbranco': '\033[7;30m'}

print('Olá muito prazer em te conhecer {}{}{}'.format(
    cores['pretoEbranco'], 'Diego', cores['pretoEbranco']+'\033[m'))

# 0 -> texto normal
# 1 -> texto negrito
# 4 -> texto sublinhado
# 7 -> inverte a sequencia

# cores de texto
# 30 -> branco
# 31 -> vermelho
# 32 -> verde
# 33 -> amarelo
# 34 -> azul
# 35 -> lilás
# 36 -> ciano
# 37 -> cinza

# cores de fundo
# 40 -> branco
# 41 -> vermelho
# 42 -> verde
# 43 -> amarelo
# 44 -> azul
# 45 -> lilás
# 46 -> ciano
# 47 -> cinza
