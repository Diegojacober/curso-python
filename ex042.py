r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))

print('-='*20,'\n Analisador de triâgulos \n', '-='*20)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    if r1 == r2 == r3:
        print('O triângulo formado é um equilátero')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('O triângulo formado é um isósceles')
    else:
        print('O triângulo formado é um escaleno')
else:
    print('Os segmentos digitados não podem formar um triângulo')