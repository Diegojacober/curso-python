# + adição
# - subtração
# * multiplicação
# / divisão
# ** Potência
# // divisão inteira
# % módulo(resto da divisão)
# == igual
#pow(4,3) == 4**3

#str+str = strstr
# 'str'*5 = strstrstrstrstr
# print('='*20) ====================
nome = input('Qual seu nome?')
print('Prazer em te conhecer {:20}!'.format(nome)) #vai dar 20 espaços e escrever
print('Prazer em te conhecer {:>20}!'.format(nome)) #vai dar 20 espaços e escrever alinhado a direita
print('Prazer em te conhecer {:<20}!'.format(nome)) #vai dar 20 espaços e escrever alinhado a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) #vai dar 20 espaços e escrever centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome)) #vai dar 20 espaços e escrever centralizado entre os iguais. Funciona com qualquer caracter
print('Prazer \n em te conhecer {}!'.format(nome),end=' ') #vai quebrar a linha no \n e escrever no final da linha
print('Continuando na mesma linha') #vai escrever no final da linha