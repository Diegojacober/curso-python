"""
Cria funções que duplicam, triplicam e quadriplicam o numero recebido como parametro
"""

def criar_multiplicardor(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicardor(2)
triplicar = criar_multiplicardor(3)
quadriplicar = criar_multiplicardor(4)

for numero in [1, 2, 3, 4, 5, 6, 7, 8]:
    print(f'*2 = {duplicar(numero)}, *3 = {triplicar(numero)}, *4 = {quadriplicar(4)}'.center(50))
    print('='*50)