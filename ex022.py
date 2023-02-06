nome = input('Digite seu nome completo: ')
nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
tamanho = len(nome) - nome.count(' ')
nomeSplit = nome.split()

print(f'Seu nome é {nome} \n Em Caps-Lock fica {nomeMaiusculo} \n Em Lower fica {nomeMinusculo} \n Tem ao todo {tamanho} letras \n Seu primeiro nome é {nomeSplit[0]} e tem {len(nomeSplit[0])} letras')
