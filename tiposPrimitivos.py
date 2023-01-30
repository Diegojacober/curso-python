#n1 = int(input('Digite um valor'))
#n2 = int(input('Digite outro valor'))
# str(),bool(),int(),float()
n1 = float(input('Digite um valor'))
n2 = float(input('Digite outro valor'))

s = n1 + n2
# print(type(n1))
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

# Dizer se é numérico
n = input('Digite Algo')
# se é numérico
print(n.isnumeric())
# se são letras
print(n.isalpha())
# se são letras e numeros
print(n.isalnum())
# se está somente em letras maiusculas
print(n.isupper())
# existem diversas outras funções para tipos de dados
