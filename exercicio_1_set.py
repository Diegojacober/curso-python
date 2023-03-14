lista_de_numeros_inteiros = [[1,1,2,3,4,5], [1,2,3,3,4,2], [1,2,3,4,2,1], [1,2,3,4,5,6,7,8,9]]

def encontrar_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1
    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero)
    
    print()
    print()
    return primeiro_duplicado
    
    
for lista in lista_de_numeros_inteiros:
    print(lista,encontrar_primeiro_duplicado(lista))