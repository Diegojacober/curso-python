"""
------------------------------Jogo da forca com python------------------------------
# Tema: Partes do corpo humano
# 6 vidas, chances de errar
# Listar letras erradas
#Listas letras acertadas
# Modos de jogo: Fácil (Nutella), Médio (Café com Leite), Dificil (Raiz)

Fácil -> Dica a cada vida perdida
Médio -> Dica a 2 vidas perdidas
Difícil -> Sem dicas
"""
import forca

forca.cabecalho('Bem vindo ao jogo da forca com Python!', 32, 32)
palavra, dificuldade = forca.sortear_palavra()

# print('A palavra sorteada é {}'.format(palavra))
forca.jogo(palavra, dificuldade)
