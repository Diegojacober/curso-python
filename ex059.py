import random

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opcao = int(input('Digite o numero de uma opção: \n[ 1 ] - Somar \n[ 2 ] - Multiplicar\n[ 3 ] - Maior\n[ 4 ] - Novos números \n[ 5 ] sair do programa\nQual sua opção? '))

while True:
    if opcao == 1:
        print('A soma entre {} e {} é {} \n \n \n'.format(n1, n2, n1 + n2))
        opcao = int(input('Digite o numero de uma opção: \n[ 1 ] - Somar \n[ 2 ] - Multiplicar\n[ 3 ] - Maior\n[ 4 ] - Novos números \n[ 5 ] sair do programa\nQual sua opção? '))

    elif opcao == 2:
        print('A multiplicação entre {} e {} é {} \n \n \n'.format(n1, n2, n1 * n2))
        opcao = int(input('Digite o numero de uma opção: \n[ 1 ] - Somar \n[ 2 ] - Multiplicar\n[ 3 ] - Maior\n[ 4 ] - Novos números \n[ 5 ] sair do programa\nQual sua opção? '))
    elif opcao == 3:
        if n1 < n2:
            print('\n O maior entre {} e {} é {} \n \n \n'.format(n1, n2, n2))
            opcao = int(input(
                'Digite o numero de uma opção: \n[ 1 ] - Somar \n[ 2 ] - Multiplicar\n[ 3 ] - Maior\n[ 4 ] - Novos números \n[ 5 ] sair do programa\nQual sua opção? '))
        elif n2 < n1:
            print('O maior entre {} e {} é {} \n \n \n'.format(n1, n2, n1))
            opcao = int(input(
                'Digite o numero de uma opção: \n[ 1 ] - Somar \n[ 2 ] - Multiplicar\n[ 3 ] - Maior\n[ 4 ] - Novos números \n[ 5 ] sair do programa\nQual sua opção? '))
        elif n2 == n1:
            print('Os dois numeros são iguais \n \n \n')
            opcao = int(input(
                'Digite o numero de uma opção: \n[ 1 ] - Somar \n[ 2 ] - Multiplicar\n[ 3 ] - Maior\n[ 4 ] - Novos números \n[ 5 ] sair do programa\nQual sua opção? '))
    elif opcao == 4:
        n1 = random.randint(0, 99999)
        n2 = random.randint(0, 99999)
        print('os novos numeros agora são {} e {} \n \n \n'.format(n1, n2))
        opcao = int(input( 'Digite o numero de uma opção: \n[ 1 ] - Somar \n[ 2 ] - Multiplicar\n[ 3 ] - Maior\n[ 4 ] - Novos números \n[ 5 ] sair do programa\nQual sua opção? '))
    elif opcao == 5:
        exit()
    else:
        print('Opção inválida, tente novamente \n \n \n')
        opcao = int(input('Digite o numero de uma opção: \n[ 1 ] - Somar \n[ 2 ] - Multiplicar\n[ 3 ] - Maior\n[ 4 ] - Novos números \n[ 5 ] sair do programa\nQual sua opção? '))