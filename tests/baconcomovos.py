"""
1 - Receber um número inteiro
2 - Saber se o número é multiplo de 3 e 5
3 - Saber se o múmero é multiplo de somente 3:
    Bacon
4 - Saber se o número é multiplo de somente 5:
    Ovos
5 - Saber se o número NÃO é multiplo de 3 a 5:
    Passa fome
"""

def bacon_com_ovos(n: int):
    assert isinstance(n, int), 'n deve ser int'
    
    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
    
    if n % 3 == 0:
        return 'Bacon'
    
    if n % 5 == 0:
        return 'Ovos'
    
    return 'Passar fome'
    
