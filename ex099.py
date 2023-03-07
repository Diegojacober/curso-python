from random import randint
def maior(* num):
    maiorNumero = 0
    for i in num:
        if i > maiorNumero:
            maiorNumero = i
        else:
            continue
    print(f'Foram passados {len(num)}, são eles [{num}], e o maior entre eles é o {maiorNumero}')
    print('-=' * 50)

maior(7,8,9,6,3,5)
maior(randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))