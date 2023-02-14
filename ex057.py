opc = input('Informe seu sexo: [M/F] ').upper().strip()[0]

# while sexo not in 'MmFf':
while opc != 'M' and opc != 'F':
    opc = input('Dados inválidos. Por favor, informe seu sexo: ').upper().strip()[0]
print('Sexo {} registrado'.format(opc))