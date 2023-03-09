def aumentar(valor,porcentagem,format=False,formatacao='R$'):
    aumento = valor * (porcentagem / 100)
    if format:
        return moeda(valor+aumento,formatacao)
    return valor + aumento


def diminuir(valor,porcentagem,format=False,formatacao='R$'):
    desconto = valor * (porcentagem / 100)
    if format:
        return moeda(valor - desconto,formatacao)
    return valor - desconto


def dobro(valor,format=False,formatacao='R$'):
    if format:
        return moeda(valor * 2,formatacao)
    return valor * 2


def metade(valor,format=False,formatacao='R$'):
     if format:
        return moeda(valor/2,formatacao)
     return valor/2

def moeda(valor=0,moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')
    
