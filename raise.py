"""
lançando erros
erros possiveis -> https://docs.python.org/3/library/exceptions.html
"""

def divide(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        # nunca comprimir o erro
        #aqui pode salvar em um arquivo de log
        # ele entende que estou relançando a exceção mas se quiser posso lançar outra
        raise

print(divide(8, 0))

# raise ValueError('Erro')