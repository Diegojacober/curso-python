for p in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(p)))
    if p == 1:
        mnPeso = 0.00
        mmPeso = 0.00
    else:
        if peso > mmPeso:
            mmPeso = peso
        if peso < mnPeso:
            mnPeso = peso
print('O menor peso é de {}Kg e o maior é de {}Kg'.format(mnPeso,mmPeso))