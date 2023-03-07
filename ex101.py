from datetime import datetime
def voto(ano):
    idade = datetime.now().year - ano

    if (idade >= 16 and idade < 18) or idade >= 65:
        return 'Voto opcional'
    elif idade >= 18:
        return 'Voto obrigatório'
    else:
        return 'Não vota'

estado = voto(int(input('Digite o ano do seu nascimento: ')))
print(estado)