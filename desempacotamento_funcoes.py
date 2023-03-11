string = 'ABCD'
lista = ['Diego', 'Angelo', 1,2 ,3 , 'Alencar']
tupla = 'Python', 'é', 'legal'

a, b, *_, p,u = lista

print(f'primeiro {a} \nsegundo {b}, \npenultimo {p} \nultimo {u}')

for nome in lista:
    print(nome, end=' ')
print()
    
print(*string)
print(*lista)
print(*tupla)