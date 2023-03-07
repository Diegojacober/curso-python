################ INTERACTIVE HELP  ################
#help()
#help(print)

# print(input.__doc__)
# print(sorted.__doc__)

################  DOCSTRING  ################
def contador(i,f,p):
    """
        -> Esta função faz uma contagem do parametro i até o parametro f pulando de acordo com a quantidade colocado no parametro p
        :param i: inicio da contagem
        :param f: final da contagem
        :param p: passo da contagem
        :return: sem retorno
    """
    c = i 
    while c <= f:
        print(f'{c}', end='.. ')
        c += p
    print('FIM')

contador(2, 10, 2)
help(contador)

################  PARAMETROS OPCIONAIS  ################
def somar(a, b, c = 0):
    s = a+b+c
    print(f'A soma vale {s}')
somar(5,8)
somar(8,9,6)
