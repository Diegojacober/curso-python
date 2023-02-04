import math
ca = float(input('Digite a medida do cateto adjacente: '))
co = float(input('Digite a medida do cateto oposto: '))
# hip = math.pow(ca, 2) + math.pow(co, 2)
hip = math.pow(co, ca)
print('A hipotenusa vale: {:.2f}'.format(hip))
