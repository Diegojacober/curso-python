## https://random-word-api.herokuapp.com/word?length=10
"""
Api que retorna a palavra aleatória gerada, a dificuldade do jogo sera baseado de acordo com o tamanho da palavra
Após pegar a palavra utilzar a api https://api.dictionaryapi.dev/api/v2/entries/en/orange onde sera pego a dica para a palavra

Sera criado um ranking com nome e pontuação por jogador,
letra acertada no nivel facil = +10 pontos
letra acertada no nivel medio = +15 pontos 
letra acertada no nivel dificil = +20 pontos 
"""
import inquirer, requests, emoji, random, os
from PIL import Image
from time import sleep

PROXIES_BOSCH = {
    'http' : 'http://ct67ca:23%23INDUSTRIAdigital@proxy.br.bosch.com:8080',
    'https' : 'https://ct67ca:23%23INDUSTRIAdigital@proxy.br.bosch.com:8080'
}

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
                    choices=['Play', 'List rules'],
                ),
    ]
    answers = inquirer.prompt(questions)
    return name,answers

def get_random_word_csv():
    path = 'ExerciciosBosch/jogo_da_forca/words.csv'
    with open(path,'rt', encoding='utf8') as archive:
        words = archive.readlines()
        word_list = random.choice(list(words))
        data = word_list.split(';')
        word = data[0]
        tip = data[1].replace('\n','')
        return word, tip
    
def write_words(word,tip):
    path = 'ExerciciosBosch/jogo_da_forca/words.csv'
    sentence = f'\n{word.upper()};{tip.upper()}'
    with open(path,'a+', encoding='utf8') as archive:
       archive.seek(0,0)
       archive.write(sentence)

def delete_archive(path):
    os.unlink(path=path)

def delete_word():
      word = input('What word do you want delete? ').upper()
      path = 'ExerciciosBosch/jogo_da_forca/words.csv'
      a = open(path,'r+',encoding='utf8')
      words = list(a.readlines())
      a.close()
      for w in words:
            data = w.split(';')
            print(data)
            data_word = data[0]
            if data[0] != '\n':
                data_tip = data[1].replace('\n','')
                if data_word == word.strip():
                    try: 
                        words.remove(f'{word.strip()};{data_tip}\n')
                    except:
                        words.remove(f'{word.strip()};{data_tip}')
                    delete_archive(path)
                    b = open(path,'a+', encoding='utf8')
                    for wd in words:
                        b.write(wd)
                    b.close()
                else:
                    print(f'{data_word} != {word}')
      

def get_word(level, lang='en'):
    while True:
        tip = ''
        word = ''
        if level == 'Nutella':
            request = requests.get(f'http://random-word-api.herokuapp.com/word?length=5&lang={lang}',proxies=PROXIES_BOSCH)
            json = request.json()
            word = json[0]
            try : 
                tip = get_tip(word=word)
            except: 
                print('Não foi encontrada a palavra {} pulando para a proxima'.format(word))
                continue
            else:
                return tip,word
        elif level == 'Coffe with milk':
            request = requests.get(f'http://random-word-api.herokuapp.com/word?length=7&lang={lang}',proxies=PROXIES_BOSCH)
            json = request.json()
            word = json[0]
            try : 
                tip = get_tip(word=word)
            except: 
                continue
            else:
                return tip,word
        elif level == 'Source':
            request = requests.get(f'http://random-word-api.herokuapp.com/word?length=10&lang={lang}',proxies=PROXIES_BOSCH)
            json = request.json()
            word = json[0].upper()
            try : 
                tip = get_tip(word=word)
            except: 
                continue
            else:
                return tip,word
        elif level == 'Custom':
            print('Welcome to the custom mode, you can add words and tips or play with the registered words')
            option = [
            inquirer.List('option',
                        
                            message=f"What you want, {name} ? ",
                            choices=['Play with the registered words', 'Add words and tips', 'Delete a word'],
                        ),
            ]
            options = inquirer.prompt(option)
            option = options['option']
            if option == 'Play with the registered words':
                word_csv, tip_csv = get_random_word_csv()
                return word_csv, tip_csv
            elif option == 'Add words and tips':
                words_quantity = int(input('How many words do you want to enter: '))
                for i in range(words_quantity):
                    print("\x1b[2J\x1b[1;1H", end="")
                    word = input('\nWhats the word? ')
                    tip = input('Whats the tip? ')
                    write_words(word=word,tip=tip)
                print('Your words was entered')
                continue
            elif option == 'Delete a word':
                delete_word()
                continue


def get_tip(word):
    while True:
        request = requests.get(f'http://api.dictionaryapi.dev/api/v2/entries/en/{word}',proxies=PROXIES_BOSCH)
        json = request.json()
        return json[0]['meanings'][0]['definitions'][0]['definition']
        
            
def get_level(name):
    questions = [
    inquirer.List('level',
                  
                    message=f"Which is your level, {name}? ",
                    choices=['Nutella', 'Coffe with milk', 'Source', 'Custom'],
                ),
    ]
    level = inquirer.prompt(questions)
    return level['level']


def get_kick(tip):
    while True:
            chance = input('\n Type it a letter: ').upper().strip()
            if chance.isnumeric() or chance == '' or chance == ' ':
                print('Please, TYPE IT A LETTER')
            else: 
                if chance == 'TIP':
                    print(f'Tip is: {tip}')
                    continue
                chance = chance[0]
                return chance

def print_informations(lifes,correct_letters,incorret_letters):
    """
    -> Exibe as informações necessárias para continuar o jogo para o usuário

    Args:
        vidas (int): quantidade de vidas que o usuário tem
        letras_corretas (array): letras corretas digitadas pelo o usuário
        letras_erradas (array): letras incorretas digitadas pelo o usuário
        :return: No Return
    """
    print("\x1b[2J\x1b[1;1H", end="")
    line()
    print(emoji.emojize(f"you have {lifes} :red_heart:", variant="emoji_type"))
    print(f'\033[37mFor see the tip, type it "tip"\033[m')
    print(f'\033[37mCorrect letters {correct_letters}\033[m')
    print(f'\033[37mIncorrect letters {incorret_letters}\033[m')
    line()


def play(name):
    
    level = get_level(name=name)
    word,tip = get_word(level=level)
    word = str(word).upper()
    print(word)
    
    lifes = 6
    # 0 -> letras chutadas corretas, 1 -> letras chutadas incorretas
    letters = [[], []]
    chance = ''
    while True:
        if lifes <= 0:
            lifes = 0
            print(f'You died - the correct word was" {word}')
            img = Image.open('ExerciciosBosch/jogo_da_forca/lose.png')
            img.show()
            break
        if len(letters[0]) == len(word):
            header(emoji.emojize(f":party_popper: :partying_face: CONGRATULATION {name},YOU WIN :partying_face: :party_popper:", variant="emoji_type"))
            img = Image.open('ExerciciosBosch/jogo_da_forca/win.gif')
            img.show()
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
            chance = get_kick(tip=tip)          
            
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
play(name=name)