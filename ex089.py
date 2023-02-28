alunos = []
while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

    cont = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if cont in 'Nn':
        break
print('-='*40)
print(f'{"ID.":<4}{"NOME":<10}{"MÉDIA":>4}')
print('-' * 26)
for c, n in enumerate(alunos):
    print(f"{c:<4}{n[0]:<10}{n[2]:>8}")
print('-' * 26)
id = int(input('Digite o ID do aluno o qual deseja ver as notas: '))
if id < 0 or id > len(alunos):
    print('ID inválido')
else:
    print(f'Notas de {alunos[id][0]}: \n\t{alunos[id][1][0]} \n\t{alunos[id][1][1]}')

