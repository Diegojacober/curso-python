from calculadora import soma

try:
    print(soma('15', 15))
except AssertionError as e:
    print(f'Conta inválida: {e}')
    