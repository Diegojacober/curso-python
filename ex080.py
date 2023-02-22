lista = list()
for i in range(5):
    n = int(input('Digite um número inteiro: '))
    if i == 0 or n < min(lista):
        lista.insert(0,n)
        print('Inserido no começo da lista')
    elif n > max(lista):
        lista.append(n)
        print('Inserido no fim da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]: 
                lista.insert(pos,n)
                print(f'Inserido na posição {pos} da lista')
                break
            pos += 1
print(lista)
        