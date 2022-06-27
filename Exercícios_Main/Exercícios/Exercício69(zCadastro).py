maior = homem = mulher = 0
while True:
    print('-' * 40)
    print('Vamos cadastrar uma pessoa!')
    print('-' * 40)
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    continuar = input('Deseja cadastrar outra pessoa? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
print(f'Total de pessoas maiores de idade: {maior}')
print(f'Número de homens cadastrados: {homem}')
print(f'Número de mulheres com menos de 20 anos: {mulher}')


    