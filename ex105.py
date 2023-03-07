def notas(*notas, sit=False):
    """
        -> Esta função recebe as notas da sala, e a informação se deseja informação a situação da sala
        calcula a media, identifica o menor e o maior valor e depois retorna um dicionario com as informações
    """
    notasdict = {'maior' : max(notas), 'menor' : min(notas)}
    total = 0
    for nota in notas:
        total += int(nota)
    notasdict['media'] = total/len(notas)
    if sit:
        if notasdict['media'] < 6:
            notasdict['situacao'] = 'RUIM'
        elif notasdict['media'] < 8:
            notasdict['situacao'] = 'NORMAL'
        elif notasdict['media'] <= 10:
            notasdict['situacao'] = 'ÓTIMA'
    return notasdict
    
sala = notas(9,9,10,10,sit=True)
print(sala)