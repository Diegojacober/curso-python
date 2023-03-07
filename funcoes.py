def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

titulo('    APRENDENDO PYTHON    ')
titulo('    PYTHON É LEGAL  ')

def soma(a, b):
    s = a + b
    print(f'A soma entre {5} e {8} é {s}')

soma(b =5,a = 8)

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(5,8,9,6,31,1)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [2,5,9,6,8]
dobra(valores)
print(valores)

def soma2(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando todos os valores {valores} temos {s}')

soma2(2,5,6,9,8,7)