#Sets - Conjunto em Python (tipo set)
"""
Representados graficamente pelo diagrama de venn
Sets em Python são mutaveis, porém aceitam apenas
tipos imutáveis como valor interno


criando um set -> set(iterável) ou {1,2,3}

Sets são eficientes para remover valores duplicados de iteráveis
*** eles não tem índexes
*** eles não garantem ordem
*** eles são iteraveis(for, in, not in)
"""

# s1 = set('Diego') # cada letra vira um valor
s1 = {'Diego',1,2,3} # a palavra é um valor completo e os numeros cada um é um
print(s1)


#Sets são eficientes para remover valores duplicados de iteráveis pois seus valores sempre serão unicos
# set_1 = {1, 2, 3, 4, 5, 5, 5, 5, 5, 5}
l1 = [1,2,3,4,5,5,5,5,5,5,5]
set_1 = set(l1)
l2 = list(set_1)
print(l2)

print(5 in set_1)

for numero in set_1:
    print(numero)
    

# Métodos uteis: add, update, clear, discard

s2 = set()
s2.add('Diego')
s2.add(1)
s2.update(('olá mundo',1 , 2, 3, 4))
# s2.clear() # limpa o set
s2.discard('Diego')
print(s2)

"""
Operadores úteis:
união | união (union) - Une
intersecção & (intersection) - itens presentes em ambos
diferença - itens presentes apenas no set da esquerda
diferença simétrica ^ - itens que não estão em ambos
"""

s4 = {1,2,3}
s5 = {2,3,4}
s6 = s4.union(s5)
s6 = s4 | s5
s6 = s4 & s5
print(s6)

#mostra o 4 -> direita
s7 = s5 - s4
# mostra o 1 --> esquerda
s7 = s4 - s5
print(s7)

s8 = s4 ^ s5
print(s8)

#Exemplo de uso dos sets

letras = set()
l = 'z'
while True:
    letra = input('Digite: ').lower()
    letras.add(letra) 
    print(letras)
    if l in letras:
        print('PARABÉNS')
        break
 