numeros = (int(input('Digite o primeiro numero: ')),
           int(input('Digite o segundo numero: ')),
           int(input('Digite o terceiro numero: ')),
           int(input('Digite o quarto numero: ')))

print(f'Voce digitou o número nove {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'A primeira vez que o número 3 apareceu foi na posição {numeros.index(3)}')
else:
    print('O número 3 não foi digitado nenhuma vez')
    
print('Os numeros pares digitados foram: ',end='')
for n in numeros:
    if n % 2 == 0:
        print(n,end=' ')