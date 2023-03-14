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

#mapear dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

# novos_produtos = [{'nome': produto['nome'], 'preco_imposto': produto['preco'] * 2.5} for produto in produtos]

novos_produtos = [{**produto, 'preco': (produto['preco'] * 1.10)} if produto['preco'] > 20 else {**produto} for produto in produtos]

print(*novos_produtos, sep='\n')