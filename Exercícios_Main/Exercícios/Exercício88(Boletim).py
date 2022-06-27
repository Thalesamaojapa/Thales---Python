from time import sleep
temp = list()
boletim = list()
while True:
    temp.append(input('Nome: '))
    temp.append(int(input('Nota 1: ')))
    temp.append(int(input('Nota 2: ')))
    boletim.append(temp[:])
    temp.clear()
    continuar = input('Deseja adicionar outro aluno? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)
for c in range(0, len(boletim)):
    nota1 = boletim[c][1]
    nota2 = boletim[c][2]
    média = (nota1 + nota2) / 2
    print(f'{c:<4}{boletim[c][0]:<10}{média:>8}')
    sleep(0.15)
print('-' * 26)
while True:
    aluno = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    elif aluno <= len(boletim) - 1:    
        print(f'As notas de {boletim[aluno][0]} são: {boletim[aluno][1:3]}')
    else:
        print('Aluno não encontrado!')

    
