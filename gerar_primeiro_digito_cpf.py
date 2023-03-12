"""
CPF: 123.456.789-10
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

EX: 764.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
    7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0
    
SOmar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resuldado por 10
301 * 10 = 3010
Obter o resto da divisao da conta por 11
3010 % 11 = 7
Se o resultado for maior que 9:
    o resultado é 0
Caso o contrário:
    o resultado é ele mesmo
    
o primeiro digito do CPF é 7
"""
def verificar_primeiro_digito_cpf(cpf):
    total = 0
    nove_digitos = cpf[:9]
    contador_regressivo = 10
    
    for digito in nove_digitos:
        multiplicacao = int(digito) * contador_regressivo
        total += multiplicacao
        contador_regressivo -= 1
    
    total = (total * 10) % 11
    
    return total if total <= 9 else 0
    
        
print(verificar_primeiro_digito_cpf('57881195029'))