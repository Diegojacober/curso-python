# Todo generator é um iterator mas o iterator não é um generetor

#Generators expression são funções que pausam


#ja está na memoria
listcoompression = [n for n in range(10)]
print(listcoompression)



generator = (n for n in range(10))
print(generator)