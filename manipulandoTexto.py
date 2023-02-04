frase = 'Aquele carro é amarelo e baixo'
print(frase[9])
# imprime o caracter 9
print(frase[9:13])
# imprime do caracter 9 á 12
print(frase[9:13:2])
# imprime do caracter 9 a 13 a cada 2
print(frase[:5])
# começa normalmente no caracter 0 e vai até o caracter 4
print(frase[9:])
# imprime do caracter 9 e vai até o fim
print(frase[9::3])
# imprime do 9 até o final pulando a cada 3
len(frase)
# retorna o tamanho
frase.count('o')
# conta quantas vezes aparece a letra o minúscula
frase.count('o', 0, 13)
# conta quantas letras o minuscula tem entre o caracter 0 e 12
frase.find('rro')
# retorna o caracter inicial da sentença
frase.find('corsa')
# retorna -1 porque não existe na frase
frase.replace('baixo', 'rápido')
# procura e substitui
frase.upper()
# deixa em maiusculo
frase.lower()
# deixa em minusculo
frase.capitalize()
# somente o primeiro caracter em maiusculo
frase.title()
# a primeira letra de cada palavra em maiusculo
frase2 = '   teste   '
frase2.strip()
# vai remover os espaços
frase2.rstrip()
# remove apenas os últimos espaços
frase2.lstrip()
# remove apenas os primeiros espaços
frase.split()
# cada palavra vira um array dentro de outro array -- separados pelo espaço
'-'.join(frase)
# junta todos os elementos, invés do espaço, utiliza o que foi colocado
