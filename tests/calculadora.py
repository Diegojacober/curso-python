def soma(x, y):
    #Assertions, geralmente é para outros desenvolvedores
    # se rodar o arquivo com -O desativa as assertions
    
    # Aqui é utilizando o doctest, em cima os valores e em baixo o que estou esperando
    """
    >>> soma(10, 20)
    30
    
    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: X precisa ser int ou float
    
    >>> soma(-10, 20)
    10
    """
    assert isinstance(x, (int, float)), 'X precisa ser int ou float'
    assert isinstance(y, (int, float)), 'Y precisa ser int ou float'
    return x + y


def subtrai(x, y):
    
    """
    >>> subtrai(10, 5)
    5
    """
    assert isinstance(x, (int, float)), 'X precisa ser int ou float'
    assert isinstance(y, (int, float)), 'Y precisa ser int ou float'
    return x - y

if __name__ == "__main__": 
    import doctest
    doctest.testmod(verbose=True)
