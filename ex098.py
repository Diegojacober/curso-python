from time import sleep
def contagem(inicio, fim, passo):
    print(f'Contagem do {inicio} até o {fim} de {passo} em {passo}')

    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM')
    print()

contagem(0, 10, 1)
contagem(0, 10, 2)
print('Agora é sua vez: ')
contagem(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))