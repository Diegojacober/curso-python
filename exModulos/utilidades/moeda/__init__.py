def aumentar(valor, porcentagem=10, format=False, formatacao='R$'):
    aumento = valor * (porcentagem / 100)
    if format:
        return moeda(valor + aumento, formatacao)
    return valor + aumento


def diminuir(valor, porcentagem=10, format=False, formatacao='R$'):
    desconto = valor * (porcentagem / 100)
    if format:
        return moeda(valor - desconto, formatacao)
    return valor - desconto


def dobro(valor, format=False, formatacao='R$'):
    if format:
        return moeda(valor * 2, formatacao)
    return valor * 2


def metade(valor, format=False, formatacao='R$'):
    if format:
        return moeda(valor / 2, formatacao)
    return valor / 2


def resumo(valor, porcentagem=10, format=False, formatacao='R$'):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print(f'PREÇO ANALISADO: \t {moeda(valor)}')
    print(f'DOBRO DO VALOR: \t {dobro(valor, format, formatacao)}')
    print(f'A METADE DO VALOR É \t {metade(valor, format, formatacao)}')
    print(f'O VALOR COM DESCONTO DE 10% É \t {diminuir(valor, porcentagem, format, formatacao)}')
    print(f'O VALOR COM AUMENTO DE 10% É \t {aumentar(valor, porcentagem, format, formatacao)}')
    print('-' * 30)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

