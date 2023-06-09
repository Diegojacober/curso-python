# datetime(ano, mes, dia)
# datetime(ano, mes, dia, horas, minutos, segundos)
# datetime.tostrptime('DATA', 'formato')
from datetime import datetime, timedelta
from pytz import timezone

data_str_data = '2023-06-09 15:08:35'
data_str_fmt =  '%Y-%m-%d %H:%M:%S.%f'
data = datetime.strptime(str(datetime.now()), data_str_fmt)


data = datetime.now(timezone('America/Sao_Paulo'))
print(data)

print(datetime.now().timestamp()) # unix da minha data
print(datetime.fromtimestamp(1686334879.832517))
# data = datetime.now(timezone('Asia/Tokyo'))
# print(data)


data_inicio = datetime.fromtimestamp(1686334879.832517)
data_fim = datetime.fromtimestamp(1686335256.570466)
delta = data_fim - data_inicio
print(delta.days, delta.min, delta.seconds)