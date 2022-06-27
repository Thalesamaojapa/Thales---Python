pessoal = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear
    pessoa['Nome'] = input('Nome: ').capitalize()
    pessoa['Sexo'] = input('Sexo: [M/F] ').upper().strip()[0]
    if pessoa['Sexo'] not in 'MF':
        while pessoa['Sexo'] not in 'MF':
            print('Sexo inválido! Responda apenas M ou F')
            pessoa['Sexo'] = input('Sexo: [M/F] ').upper().strip()[0]
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    pessoal.append(pessoa.copy())
    continuar = input('Deseja continuar? [S/N] ').strip()[0]
    if continuar not in 'NnSs':
        while continuar not in 'NnSs':
            print('Resposta inválida! Responda apenas S ou N')
            continuar = input('Deseja continuar? [S/N] ')
    if continuar in 'Nn':
        break
média = soma / len(pessoal)
print(f'A) Ao todo temos {len(pessoal)} pessoas')
print(f'B) A média de idade do pessoal é de {média:.2f} anos')
print(f'C) As mulheres cadastradas são:', end=' ')
for ind in pessoal:
    if ind['Sexo'] in 'F':
        print(f'{ind["Nome"]}', end=' ')
print('\nD) Lista de pessoas cujas idades estão acima da média: ')
for ind in pessoal:
    if ind['Idade'] > média:
        print('     ', end='')
        for k, v in ind.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')


