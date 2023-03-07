def fatorial(n,show=False):
    tot = 1
    exp = f'{n}! = '
    for i in range(1, n+1):
        tot = tot * i
        exp += f'{i} * '
    if show == False:
        return tot
    else:
        exp = exp[0:len(exp) -2] + f'--> {tot}'
        return exp

print(fatorial(5,True))