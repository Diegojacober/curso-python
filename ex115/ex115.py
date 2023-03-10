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
        
def arq_exist(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar_arquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso')
        
def mostrar_dados(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]} - {dado[1]} anos')

def cadastrar_pessoa(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print('Teve um erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao cadastrar')
        else:
            print(f'{nome} foi cadastrado(a) com sucesso! \n')
    finally:
        a.close()
    
if __name__ == '__main__':
    arq = 'ex115/pessoas.txt'
    if not arq_exist(arq):
        print('Arquivo não encontrado')
        criar_arquivo(arq)
    else:
        print('arquivo encontrado com sucesso')
    cabecalho('SISTEMA ARQUIVO 0.0.1')
    while True:
        opc = menu(['Ver usuários', 'Cadastradar usuários', 'Sair do sistema'])
        if opc == 1:
            linha()
            mostrar_dados(arq)
            linha()
        elif opc == 2:
            cabecalho('NOVO CADASTRO')
            nome = input('Nome: ')
            idade = leiaInt('Idade: ')
            cadastrar_pessoa(arq, nome, idade)
        elif opc == 3:
            cabecalho('Saindo do sistema... Até logo!')
            break
        else:
            print('Opção inválida')
        sleep(2)
            

        