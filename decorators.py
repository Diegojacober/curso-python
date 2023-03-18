import requests
import time


# # Define nosso decorator
# def calcula_duracao(funcao):
#     def wrapper():
#         # Calcula o tempo de execução
#         tempo_inicial = time.time()
#         funcao()
#         tempo_final = time.time()

#         # Formata a mensagem que será mostrada na tela
#         print("[{funcao}] Tempo total de execução: {tempo_total}".format(
#             funcao=funcao.__name__,
#             tempo_total=str(tempo_final - tempo_inicial))
#         )

#     return wrapper

# # Decora a função com o decorator
# @calcula_duracao
# def main():
#     for n in range(0, 10000000):
#         pass

# # Executa a função main
# main()

"""
Funções decoradores e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
decoradores são usados para fazer o python
usar as funções decoradores em outras funções
"""

#função decoradora
# def criar_funcao(func):
    
#     def interna(*args, **kwargs):
#         for arg in args:
#             is_string(arg)
#         resultado = func(*args, **kwargs)
#         #
#         return resultado
#     return interna


# def is_string(param):
#     if not isinstance(param,str):
#         raise TypeError('param deve ser uma string')


# @criar_funcao
# def invert_string(string) -> str:
#     print(invert_string.__name__)
#     return string[::-1].upper()

# invert_string_checando_parametro = criar_funcao(invert_string)
    
# invertida = invert_string_checando_parametro('123')
# print(invertida)

#Decoradora com parametros

# def fabrica_de_decoradores(a=None, b=None, c=None):

#     def fabrica_de_funcoes(func):
#         print('Decoradora 1 ')
        
#         def inner_function(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return result
#         return inner_function
#     return fabrica_de_funcoes



# @fabrica_de_decoradores(1,2,3)
# def soma(x,y):
#     return x + y
    

# conta_1 = soma(10,5)
# print(conta_1)

# multiplica = fabrica_de_decoradores()(lambda x, y: x * y)
# dez_vezes_cinco = multiplica(5,10)
# print(dez_vezes_cinco)

# def calcular_tempo(funcao):
#     def wrapper():
#         tempo_inicial = time.time()
#         funcao()
#         tempo_final = time.time()
#         print(f"Duração foi de {tempo_final-tempo_inicial} segundos")
#     return wrapper

# @calcular_tempo
# def pegar_cotacao_dolar():
#     link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
#     requisicao = requests.get(link)
#     requisicao = requisicao.json()
#     print(requisicao['USDBRL']['bid'])

# pegar_cotacao_dolar()