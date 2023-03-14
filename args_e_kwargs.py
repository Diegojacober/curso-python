a,b = 1,2 
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Erling',
    'sobrenome': 'Halaand',
}

dados_pessoa = {
    'idade': 19,
    'altura': 1.92
}

a,b = pessoa.items()


pessoa_completa = {**pessoa,**dados_pessoa, 'profissão': 'jogador'}
# print(pessoa_completa)

# kwargs - keywords arguments (argumentos nomeados)

def mostrar_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)
    for chave, valor in kwargs.items():
        print(f'{chave} = {valor}')
    
mostrar_argumentos_nomeados(1,nome='Diego',qualquer=132)