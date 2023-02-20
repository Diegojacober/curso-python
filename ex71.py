print('=' * 30)
print('{:^30}'.format('BANCO DAJ'))
print('=' * 30)
valor = int(input('Qual valor você quer sacar? '))
total = valor
ced = 50
totCedula = 0
while True:
    if total >= ced:
        total -= ced
        totCedula += 1
    else:
        if totCedula > 0:
            print(f'Total de {totCedula} cédulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totCedula = 0
        if total == 0:
            break
print('='*30)
print('{:^30}'.format('Volte sempre!'))
print('='*30)