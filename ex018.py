from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'o ângulo de {angulo:.2f} tem o seno = {seno:.2f}, cosseno = {cosseno:.2f} e tangente = {tangente:.2f}')
