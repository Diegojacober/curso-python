num = [2, 5, 9, 1]

#substituir
num[2] = 3

#adicionar
num.append(7)

#inverter sequencia
num.sort(reverse=True)

#inserir na posição especifica insere o 5 na posição 2 e empurra os existentes para frente
num.insert(2, 5)

#remover de uma posição -- exclui da posição 2
num.pop(2)

#remover item, remove somente a primeira ocorrencia
num.remove(5)

if 4 in num:
    num.remove(4)
else:
    print('Número não encontrado')

#criar lista vazia ou lista = list()
lista = []
lista.append(5)
lista.append(4)
lista.append(3)

for valor in lista:
    print(f'{valor}...',end='')
for chave, valor in enumerate(lista):
    print(f'\nposição: {chave} - valor: {valor}...')
    
lista.append(int(input('Digite um valor: ')))

a = [2, 3, 4, 7, 9]
b = a
#assim mexe nas duas listas, pois não esta criando uma cópia e só igualando
b[2] = 8
print(f'lista A: {a}')
print(f'lista B: {b}')

c = [2, 3, 4, 7, 9]
d = c[:]
#assim cria uma cópia, e quando modificar, modifica somente a cópia
b[2] = 8
print(f'lista C: {c}')
print(f'lista D: {d}')