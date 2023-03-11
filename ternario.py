# Condicional de uma linha
condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 9
novo_digito = digito if digito <= 9 else 0
print(novo_digito)

print('Valor' if False else 'Outro valor' if False else 'Fim')