r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))

print('-='*20,'\n Analisador de triâgulos', '-='*20)

if r1 > r2 + r3 and r2 > r1 + r3 and r3 > r2 + r1:
    print('Os segmentos digitados podem formar um triângulo')
else:
    print('Os segmentos digitados não podem formar um triângulo')