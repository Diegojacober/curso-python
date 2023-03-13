"""
High Order Functions
Funções de primeira classe

High Order Functions -> Funções que podem receber e/ou retornar outras funções

First Class Functions -> Funções que são tratadas como outros tipos de dados comuns (Strings, Inteiros, etc...)
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(funcao, *args):
    return funcao(*args)


print(executa(saudacao, 'Bom dia', 'Diego'))

print(executa(saudacao, 'Boa noite', 'Ângelo'))