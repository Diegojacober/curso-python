def leiaInt(msg,msg2):
    ok = False
    valor = 0
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO: por favor, digite um numero inteiro válido')
            continue
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
        else:
            print(f'O número inteiro que você digitou foi {n}')
            while True:
                try:
                    r = float(input(msg2))
                except(ValueError,TypeError):
                    print('ERRO: por favor, digitte um número real válido')
                    continue
                except(KeyboardInterrupt):
                    print('Entrada de dados interrompida pelo usuário')
                else:
                    print(f'O número real que você digitou foi {r}')
                    break
        break

        
leiaInt('Digite um número inteiro: ', 'Digite um número real: ')
