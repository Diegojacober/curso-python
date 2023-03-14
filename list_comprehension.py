"""
List comprehension em Python
é uma forma rápida de criar listas a partir de iteraveis
"""

#jeito comum
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

#com comprehension
lista_1 = [(numero + 1) * 2 for numero in range(10)]
print(lista_1)