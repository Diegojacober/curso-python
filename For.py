for c in range(0,6,2):
    print(c)
print('FIm')

n = int(input('Digite um número: '))
for c in range(n+1):
    print(c)
    
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i,f+1,p):
    print(c)
    
s = 0
for c in range(0,4):
    nu = int(input('Digite um valor: '))
    s += nu
print('A soma de todos os números é {}'.format(s))