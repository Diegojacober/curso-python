#Python exceptions
# NameError
# ValueError
# ZeroDivisionError
# TypeError
# IndexError
# KeyError
# EOFError
# KeyboardInterrupt
# OSError
# MemoryError
# ConnectionError
# RuntimeError
# IndentationError

try:
    a = int(input('Numerador: '))
    n = int(input('Denominador: '))
    d = a/n
    
#se o erro for esse
except(ZeroDivisionError):
        print('Não é possivel dividir nenhum numero por 0')
#se for qualquer outro erro
except Exception as erro:
    print('Infelizmente tivemos um problema, o erro foi {} '.format(erro.__class__))
# se não for erro
else:
    print('O resultado da divisão é {:.2f}'.format(d))
# e depois de ter erro ou não, fazer isto
finally:
    print('Volte sempre! Muito obrigado!')