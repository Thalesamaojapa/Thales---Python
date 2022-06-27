
mvelho = 0
tot = 0
soma = 0
for c in range(1, 5):
    print('-' * 5,'{}º PESSOA'.format(c), '-' * 5)
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    soma = soma + idade    
    if idade >= mvelho and sexo == 'M':
        mvelho = idade
        nomemvelho = nome
    if sexo == 'F' and idade <= 20:
        tot = tot + 1
print('A média de idade do grupo é {}'.format(soma / 4))
print('O homem mais velho do grupo é {} com {} anos'.format(nomemvelho, mvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(tot))
