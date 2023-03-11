"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade(ruim)
"""
velocidade = 61 # valocidade atual do carro
local_carro = 99 #local que o carro esta na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_no_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_no_radar_1 and vel_carro_passou_radar_1

if carro_multado_radar_1:
   print('A velocidade do carro passou da permitida pelo radar 1 e foi multado')