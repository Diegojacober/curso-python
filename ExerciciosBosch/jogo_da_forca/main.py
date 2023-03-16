## https://random-word-api.herokuapp.com/word?length=10
"""
Api que retorna a palavra aleatória gerada, a dificuldade do jogo sera baseado de acordo com o tamanho da palavra
Após pegar a palavra utilzar a api https://api.dictionaryapi.dev/api/v2/entries/en/orange onde sera pego a dica para a palavra

Sera criado um ranking com nome e pontuação por jogador,
letra acertada no nivel facil = +10 pontos
letra acertada no nivel medio = +15 pontos 
letra acertada no nivel dificil = +20 pontos 
"""
import inquirer, requests, emoji
from time import sleep

def line(color=30):
    """
      -> Função que printa uma linha
    :param cor: cor da linha
    """
    print(f'\033[{color}m=\033[m'*60)

def header(txt, color_line=30, color_letter=30):
    """
    -> Função que faz um cabeçalho no terminal
    Args:
        txt (String): Texto do cabeçalho
        cor_linha (int, optional): Cor da linha de cima do cabeçalho, por padrão é branca. Defaults to 30.
        cor_letra (int, optional): Cor da linha de baixo do cabeçalho, por padrão é branca. Defaults to 30.
        :return: No return
    """
    line(color_line)
    print(f'\033[{color_letter}m{txt}\033[m'.center(60))
    line(color_line)

def name_and_option():
    while True:
        name = input("What's your name? ")
        if name not in '' and len(name) > 2:
            break
        else: 
            print('Please, write your name')
    questions = [
    inquirer.List('option',
                    message="What you want?",
                    choices=['Play', 'See the ranking', 'List rules'],
                ),
    ]
    answers = inquirer.prompt(questions)
    return name,answers


def get_word(level, lang='en'):
    while True:
        tip = ''
        word = ''
        if level == 'Nutella':
            request = requests.get(f'https://random-word-api.herokuapp.com/word?length=5&lang={lang}')
            json = request.json()
            word = json[0]
            try : 
                tip = get_tip(word=word)
            except: 
                print('Não foi encontrada a palavra {} pulando para a proxima'.format(word))
                continue
            else:
                return tip,word
        elif level == 'Café com leite':
            request = requests.get(f'https://random-word-api.herokuapp.com/word?length=7&lang={lang}')
            json = request.json()
            word = json[0]
            try : 
                tip = get_tip(word=word)
            except: 
                continue
            else:
                return tip,word
        elif level == 'Raiz':
            request = requests.get(f'https://random-word-api.herokuapp.com/word?length=10&lang={lang}')
            json = request.json()
            word = json[0].upper()
            try : 
                tip = get_tip(word=word)
            except: 
                continue
            else:
                return tip,word


def get_tip(word):
    while True:
        request = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
        json = request.json()
        return json[0]['meanings'][0]['definitions'][0]['definition']
        
            


def get_level(name):
    questions = [
    inquirer.List('level',
                    message=f"Which is your level, {name}? ",
                    choices=['Nutella', 'Café com leite', 'Raiz'],
                ),
    ]
    level = inquirer.prompt(questions)
    return level['level']


def get_kick():
    while True:
            chance = input('\n Type it a letter: ').upper().strip()
            if chance.isnumeric() or chance == '' or chance == ' ':
                print('Please, TYPE IT A LETTER')
            else: 
                chance = chance[0]
                return chance

def print_informations(lifes,correct_letters,incorret_letters,tip=0):
    """
    -> Exibe as informações necessárias para continuar o jogo para o usuário

    Args:
        vidas (int): quantidade de vidas que o usuário tem
        letras_corretas (array): letras corretas digitadas pelo o usuário
        letras_erradas (array): letras incorretas digitadas pelo o usuário
        dicas (int): quantidade de dicas que o usuário possui
        :return: No Return
    """
    print("\x1b[2J\x1b[1;1H", end="")
    line()
    print(emoji.emojize(f"Você ainda tem {lifes} :red_heart:", variant="emoji_type"))
    print(f'\033[37mVocê tem direito a {tip} dicas -- Para usar uma dica digite "dica"\033[m')
    print(f'\033[37mLetras corretas {correct_letters}\033[m')
    print(f'\033[37mLetras incorretas {incorret_letters}\033[m')
    line()


def play(name):
    level = get_level(name=name)
    tip,word = get_word(level=level)
    word = str(word).upper()
    print(word)
    
    point = 0
    lifes = 6
    # 0 -> letras chutadas corretas, 1 -> letras chutadas incorretas
    letters = [[], []]
    chance = ''
    while True:
        if lifes <= 0:
            lifes = 0
            print(f'SUAS VIDAS ACABARAM - A palavra correta era {word}')
            break
        if len(letters[0]) == len(word):
            header(emoji.emojize(":party_popper: :partying_face: PARABÉNS VOCÊ ACERTOU :partying_face: :party_popper:", variant="emoji_type"))
            break
        else:
            for letter in word:
                    try:
                        letters[0].index(letter)
                    except:
                        if letter == ' ':
                            print(' ', end=' ')
                            letters[0].append(' ')
                        else:
                            print('_', end=' ')
                    else:
                        print(letter, end=' ')
            chance = get_kick()          
            
            if chance in word:
                if chance not in letters[0]:
                    for letter in word:
                        if chance == letter: letters[0].append(chance)
                else:
                    print('You already type it this letter')
            else:
                if chance not in letters[1]:
                    letters[1].append(chance)
                    lifes -= 1
                else:
                    print('You already type it this letter')
        
            sleep(1)
            print_informations(lifes=lifes,correct_letters=letters[0],incorret_letters=letters[1])
            

name,option = name_and_option()
print(option['option'], name)
play(name=name)