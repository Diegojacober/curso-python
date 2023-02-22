expressao = input('Digite a expressão matemática: ')
pilha = []
for caracter in expressao:
    if caracter == '(':
        pilha.append('()')
    elif caracter == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')
