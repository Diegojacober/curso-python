import random, emoji, time

def linha(cor=30):
    """
      -> Função que printa uma linha
    :param cor: cor da linha
    """
    print(f'\033[{cor}m=\033[m'*60)


def cabecalho(txt, cor_linha=30, cor_letra=30):
    """
    -> Função que faz um cabeçalho no terminal
    Args:
        txt (String): Texto do cabeçalho
        cor_linha (int, optional): Cor da linha de cima do cabeçalho, por padrão é branca. Defaults to 30.
        cor_letra (int, optional): Cor da linha de baixo do cabeçalho, por padrão é branca. Defaults to 30.
        :return: No return
    """
    linha(cor_linha)
    print(f'\033[{cor_letra}m{txt}\033[m'.center(60))
    linha(cor_linha)


def sortear_palavra():
    """
    -> Função responsável por fazer interação com o usuário, garantindo que ele digite apenas as opções existentes, e sorteando a palavra do nível desejado
    :params:none
    :return: Palavra sorteada
    """
    palavras = [
        ['CABEÇA', 'TRONCO', 'LINGUA', 'BRAÇO', 'PERNA',
            'PÉ', 'DEDO', 'UNHA', 'NARIZ', 'COTOVELO'],
        ['CRÂNIO', 'CÉREBRO', 'PESCOÇO', 'NUCA', 'GLUTÉOS',
         'ORELHA', 'PULSO', 'ANTEBRAÇO', 'OMBRO', 'CORAÇÃO'],
        ['CEREBELO', 'EPIGLOTE', 'LARINGE', 'ESÔFAGO', 'VÉRTEBRA CERVICAL',
            'FÍGADO', 'PULMÃO', 'INTESTINO GROSSO', 'INTESTINO DELGADO', 'RINS']
    ]
    while True:
        print('\033[34m\nTemos 3 níveis: \n\t 1 - Nutella (Você tem direito a 5 dicas, além de palavras mais fáceis) \
              \n\t 2 - Café com leite (Você tem direito a 3 dicas, além de palavras um pouco mais difíceis) \
              \n\t 3 - Raiz (Você não recebe \033[1mNENHUMA\033[m \033[34mdica, e palavras consideradas hardcore)\033[m')
        while True:
            opcao = input('\nDigite o numero da opção que você deseja jogar: ')
            try:
                opcao = int(opcao)
            except (ValueError, TypeError):
                print(
                    '\033[31mERRO!! Digite apenas o numero da opção deseja.\033[m')
            else:
                if opcao > 3 or opcao < 1:
                    print(
                        '\033[33mATENÇÃO!! Digite apenas opções de 1 ao 3\033[m')
                    continue
                else:
                    break
        palavra = random.choice(palavras[opcao-1])
        dificuldade = opcao
        return palavra, dificuldade

def print_informacoes(vidas,letras_corretas,letras_erradas,dicas):
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
    linha()
    print(emoji.emojize(f"Você ainda tem {vidas} :red_heart:", variant="emoji_type"))
    print(f'\033[37mVocê tem direito a {dicas} dicas -- Para usar uma dica digite "dica"\033[m')
    print(f'\033[37mLetras corretas {letras_corretas}\033[m')
    print(f'\033[37mLetras incorretas {letras_erradas}\033[m')
    linha()

def jogo(palavra,dificuldade):
    """Função que faz a interação com o usuário, captura as tentaticas, verifica se o mesmo acertou, exibe as mensagens, exibe as dicas e verifica se ele acertou a palavra

    Args:
        palavra (String): palavra sorteada
        dificuldade (int): dificuldade do jogo
    """
    # armazena quantas vidas o usuário possui
    vidas = 8
    palavra = 'INTESTINO DELGADO'
    # armazena as letras que o usuario chutou, o indice 0 são as letras corretas, e o indice 1 são as letras erradas
    letras = [[], []]
    dica = 5 if dificuldade == 1 else 3 if dificuldade == 2 else 0 
    while True:
        if vidas <= 0:
            vidas = 0
            print(f'SUAS VIDAS ACABARAM - A palavra correta era {palavra}')
            break
        if len(letras[0]) == len(palavra):
            cabecalho(emoji.emojize(":party_popper: :partying_face: PARABÉNS VOCÊ ACERTOU :partying_face: :party_popper:", variant="emoji_type"))
            break
        else:
            # Exibe a palavra
            print('\t\t')
            for letra in palavra:
                try:
                    letras[0].index(letra)
                except:
                    if letra == ' ':
                        print(' ', end=' ')
                        letras[0].append(' ')
                    print('_', end=' ')
                else:
                    print(letra, end=' ')
            
            # Armazena o chute do usuário
            chute_usuario = input('\nDigite uma letra: ').strip().upper()
            # Verifica se o usuário tem dicas
            if chute_usuario == 'DICA':
                if dica > 0:
                    letras_nao_chutadas = list()
                    for letra in palavra:
                        try:                                                      
                            letras[0].index(letra)
                        except:
                            letras_nao_chutadas.append(letra)
                    dica -= 1
                    print(f'\n\033[mDICA: palavra tem a letra: {random.choice(letras_nao_chutadas)}\033[m')
                else:
                    print('Você não tem direito a dicas')
            else:
                if chute_usuario in palavra:
                    if chute_usuario not in letras[0]:
                        for letra in palavra:
                            if chute_usuario == letra: letras[0].append(chute_usuario)
                    else:
                        print('Você já digitou esta letra')
                else:
                    if chute_usuario not in letras[1]:
                        letras[1].append(chute_usuario)
                        vidas -= 1
                    else:
                        print('Você já digitou esta letra')
            
            # Tempo de delay para o usuario ler as informações
            time.sleep(1.2)
            print_informacoes(vidas=vidas, letras_corretas=letras[0], letras_erradas=letras[1],dicas=dica)