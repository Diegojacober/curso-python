# Verifica se a cidade se chama santo
c = input('Em que cidade você nasceu?  ').strip()
cidade = c.lower()
print(cidade[:5] == 'santo')