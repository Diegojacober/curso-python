caminho = 'manipulando_arquivos/arquivo.txt'

# arquivo = open(caminho,'a+')

# arquivo.close()

with open(caminho,'a+') as arquivo:
    print('olá mundo')
    
    print('o arquivo é fechado automaticamente')