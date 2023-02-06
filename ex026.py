f = input('Digite uma frase: ')
print('A letra "A" aparece {} vezes'.format(f.count('a')))
print('A primeira aparição da letra "A" é na posição {}'.format(f.find('a')+1))
print('A ultima aparição da letra "A" é na posição {}'.format(f.rfind('a')+1))