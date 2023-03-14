lista = ['a', 1, 1.1, True, [0, 1, 2], (1,2), {0,1}, {'nome': 'Diego'}]

for item in lista:
    # print(item, isinstance(item, int))
    if isinstance(item, int) : print('Um inteiro')
    elif isinstance(item, str) : print('Uma string')
    else: print(type(item))