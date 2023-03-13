"""
Metodos uteis em dicionarios

len - quantas chaves
keys - iteravel com as chaves
values - iteravel xom os valores
items - iteravel com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtem uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro
"""
import copy
# para copias profundas

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2, 3]
}

# não copia se tiver listas no dicionario
d2 = d1.copy()
d2['l1'][1] = 999
print(d1)
print(d2)

d3 = copy.copy(d1)
d3['l1'][1] = 1234
print(d3)

#get
p1 = {'nome':'Diego Alencar', 'idade': 18, 'trabalho': 'Bosch'}
print(p1['nome'])
print(p1.get('salario','Este indice não existe'))

#pop
# nome = p1.pop('nome')
# print(nome)
# print(p1)

#popitem
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

#update
# p1.update({
#     'salario': 56900,
#     'carro': 'ferrari',
#     'nome': 'Gaston',
#     'idade': 42
# })

p1.update(nome='Carlos', salario=1200)

print(p1)