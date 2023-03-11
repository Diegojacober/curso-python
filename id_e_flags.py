"""

Flag (Bandeira) -- Marcar local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

# se as variaveis forem iguais o local de memória vai ser o mesmo
v1 = 'a'
v2 = 'a'

print(id(v1))
print(id(v2)) 

#Flags

condicao = False

passou_no_if = None # Flag de passar no if
if condicao:
    passou_no_if = True
    print('Faça Algo')
else:
    print('Não Faça Algo')
    
      #mostra o valor       se a variavel é none ou não
# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')