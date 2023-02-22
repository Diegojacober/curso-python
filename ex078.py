numeros = []
for i in range (5):
    numeros.append(int(input(f'Digite o {i+1}º número: ')))

print(f'O menor número foi {min(numeros)}, e apareceu nas posições ', end='')

for c,n in enumerate(numeros):
    if n == min(numeros):
        print(f'{c+1}, ',end='')
 
print(f'\n\nO maior número foi {max(numeros)}, e apareceu nas posições ', end='')       
for c,n in enumerate(numeros):
    if n == max(numeros):
        print(f'{c+1}, ',end='')
