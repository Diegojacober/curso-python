numero = int(input('Digite um número inteiro: '))
opcao = int(input('Escolha uma das bases de conversão: \n [ 1 ] converter para BINÁRIO \n [ 2 ] converter para OCTAL \n [ 3 ] converter para HEXADECIMAL \n Sua opção: '))

if opcao == 1:
    print(f'{numero} convertido em binário fica: \n{bin(numero) [2:]}')
    # fatia os 2 primeiros digitos pois não importam
elif opcao == 2:
    print(f'{numero} convertido em octal fica: \n{oct(numero) [2:]}')
elif opcao == 3:
    print(f'{numero} convertido em hexadecimal fica: \n{hex(numero) [2:]}')
else:
    print('Você digitou uma conversão inesperada')