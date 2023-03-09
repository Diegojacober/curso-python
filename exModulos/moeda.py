def aumentar(valor,porcentagem):
    aumento = valor * (porcentagem / 100)
    return valor + aumento


def diminuir(valor,porcentagem):
    desconto = valor * (porcentagem / 100)
    return valor - desconto


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor/2

def moeda(valor=0,moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')
    
