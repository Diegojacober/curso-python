expressao = input('Digite algo')

print('O tipo primitivo desse valor é {}'.format(type(expressao)))
print('Só tem espaços?',expressao.isspace())
print('É um numero?',expressao.isnumeric())
print('É alfabético?',expressao.isalpha())
print('É alfanumérico?',expressao.isalnum())
print('Esta em upper?',expressao.isupper())
print('Esta em lower?',expressao.islower())
# maiusculas e minusculas juntas
print('Esta capitalizada?',expressao.istitle())