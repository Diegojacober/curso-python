def soma(x, y):
    #Assertions, geralmente é para outros desenvolvedores
    # se rodar o arquivo com -O desativa as assertions
    assert isinstance(x, (int, float)), 'X precisa ser int ou float'
    assert isinstance(y, (int, float)), 'Y precisa ser int ou float'
    return x + y