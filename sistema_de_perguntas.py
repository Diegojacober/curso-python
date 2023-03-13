# um quiz
import random
from time import sleep
perguntas = [
    {
        'pergunta': 'Quanto é 2²?',
        'opcoes': [2,4,6,1],
        'resposta': 2
    },
    {
        'pergunta': 'Quando começou a primeira guerra mundial',
        'opcoes': [1939,1914,1789,1880],
        'resposta': 2
    },
    {
        'pergunta': 'Onde Caio Tawfiq nasceu?',
        'opcoes': ['Londres, Brasil', 'Londres, Reino Unido', 'Londres, Inglaterra', 'Londres, Cazaquistão'],
        'resposta': 3
    },
    {
        'pergunta': 'O que é o While em programação?',
        'opcoes': ['Estrutura de decisão', 'Laço de repetição', 'Variável', 'Array'],
        'resposta': 2
    }
]

while True:
    pergunta_selecionada = random.choice(perguntas)
    print(pergunta_selecionada['pergunta'])
    for chave, opcao in enumerate(pergunta_selecionada['opcoes']):
        chave = 'A' if chave == 0 else 'B' if chave == 1 else 'C' if chave == 2 else 'D'
        print(f'({chave}) {opcao}')
    resposta = pergunta_selecionada['resposta']
    
    tentativa_usuario = input('Sua alternativa: ').upper()[0]
    tentativa = 1 if tentativa_usuario == 'A' else 2 if tentativa_usuario == 'B' else 3 if tentativa_usuario == 'C' else 'D'
    print(tentativa)
    if tentativa == resposta:
        print('Parabens você acertou')
    else:
        print('Você errou, mais sorte na próxima')
    sleep(1)
    print("\x1b[2J\x1b[1;1H", end="")
    continue 