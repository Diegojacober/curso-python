nome = input('Digite seu nome: ').strip()
tamanho_nome = len(nome)

if not nome == '' and tamanho_nome <= 4:
    print('Seu nome é curto')
elif (not nome == '') and (tamanho_nome <= 6):
    print('Seu nome é medio')
elif (not nome == '') and (tamanho_nome > 6):
    print('Seu nome é longo')
else:
    print('Nome inválido')
