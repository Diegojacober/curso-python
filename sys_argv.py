# sys.argv - Execeutando arquivos com argumentos no sistema
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você não passou nenhum argumento')
else:
    print(f'Você passou os argumentos {argumentos[0:]}')
    
#existe o argparse.ArgumentParser que é mais robusto, que trata os argumentos