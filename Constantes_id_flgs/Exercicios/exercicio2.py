def pegar_horario(msg):
    while True:
        horario = input(msg).strip()
        if horario.find(':') == -1:
            print('Erro digite no formato hh:mm')
            continue
        else:
            try:
                horario_sem_sinais = horario.replace(':','')
                horario_inteiro = int(horario_sem_sinais)
            except:
                print('Digite apenas numeros')
                continue
            else: 
                horario_minuto = horario.split(':')
                return horario_minuto
            
                   
                   
            
            
hora_completa = pegar_horario('Digite a hora de agora: ')

horas = int(hora_completa[0])
minutos = int(hora_completa[1])

manha = (horas >= 0 and horas <= 11) and (minutos <= 59)
tarde = (horas >= 12 and horas <= 17) and (minutos <= 59)
noite = (horas >= 17 and horas <= 23) and (minutos <= 59)

if manha:
    print(f'{horas}:{minutos} se diz Bom dia')
elif tarde:
    print(f'{horas}:{minutos} se diz Boa tarde')
elif noite:
    print(f'{horas}:{minutos} se diz Boa noite')
else:
    print('Horário inválido')