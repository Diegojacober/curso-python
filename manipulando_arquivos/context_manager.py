import os
caminho = 'manipulando_arquivos/arquivo.txt'

# for i in range(50):
#     with open(caminho,'a+') as arquivo:
#         arquivo.write(f'Ola {i}\n')

with open(caminho,'a+', encoding='utf8') as arquivo:
    arquivo.write('olá\n')
    arquivo.writelines(('ola \n','pessoa \n'))
    #movendo o curso para o inicio
    arquivo.seek(0,0)
    print(arquivo.read())
    
print('-'*25)
    
with open(caminho,'r') as arquivo:
    for linha in arquivo.readlines():
        print('LINHA::: ',linha.strip())
    #lendo o arquivo de uma vez
    arquivo.seek(0,0)
    print(arquivo.read())
    #movendo o curso para o inicio
    arquivo.seek(0,0)
    #lê só a linha
    print(arquivo.readline().strip())
    
# os.remove(caminho) # ou os.unlink(caminho)
# renomeia e move
# os.rename(caminho,'manipulando_arquivos/renomeando.txt')