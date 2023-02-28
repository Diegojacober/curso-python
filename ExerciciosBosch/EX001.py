import datetime
def carta(dia, mes, ano):
    current_time = datetime.datetime.now() 
    d = datetime.datetime(ano, mes, dia)
    d2 = datetime.datetime(datetime.date.today().year, current_time.month, current_time.day)
    dias = d2 - d 
    print(dias.days)
    if dias.days >= 6570:
        print('Você pode tirar cnh')
    else:
        print('Você não pode tirar cnh')
        
dia = int(input('Digite o dia que você nasceu: '))
mes = int(input('Digite o mes que você nasceu: '))
ano = int(input('Digite o ano que você nasceu: ')) 
carta(dia,mes,ano)

