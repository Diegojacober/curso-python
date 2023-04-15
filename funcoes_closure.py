"""
Closure e funções que retornam outras funções
"""

# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}!'
#     # tirar parenteses retorna a função e não a executa
#     return saudar

# dizer_bom_dia = criar_saudacao('Bom dia')
# dizer_boa_noite = criar_saudacao('Boa noite')

# # adiando a execução
# print(dizer_bom_dia('Gabriel'))
# print(dizer_boa_noite('João'))

# for nome in ['Diego', 'Cadu', 'Angelo', 'Nicole']:
#     print(dizer_bom_dia(nome))
    
    
#exercicio
#crie funções que duplicam, triplicam e quadruplicam o numero recebido como parametro

def multiplicador(multiplicador):
    def multiplicarNumero(num):
        return multiplicador * num
    return multiplicarNumero

duplicar = multiplicador(2)
print(duplicar(5))


triplicar = multiplicador(3)
print(triplicar(5))

quadruplicar = multiplicador(4)
print(quadruplicar(5))
