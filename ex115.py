from time import sleep
def linha(tam = 42):
    print('-' * 42)

def cabecalho(txt):
    linha()
    print(f'{txt}'.center(42))
    linha()
    
def leiaInt(msg):
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
            break
    return n
    

    
def menu(vetor):
    for i in range(len(vetor)):
        print(f'{i+1} - {vetor[i]}')
    linha()
    opc = leiaInt('Sua opção: ')
    return opc
        
    
    
if __name__ == '__main__':
    cabecalho('SISTEMA ARQUIVO 0.0.1')
    while True:
        opc = menu(['Ver usuários', 'Cadastradar usuários', 'Sair do sistema'])
        if opc == 1:
            print('opção 1')
        elif opc == 2:
            print('opção 2')
        elif opc == 3:
            cabecalho('Saindo do sistema... Até logo!')
            break
        else:
            print('Opção inválida')
        sleep(2)
            

        