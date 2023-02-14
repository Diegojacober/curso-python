frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('{} -- {}'.format(inverso, junto))
if inverso == junto:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
