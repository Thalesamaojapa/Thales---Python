#crie um programa que leia o nome de uma pessoa e mostre todas as letras em maiusculo, minusculo
#quantas letras tem nesse nome(sem espaço) e quantas letras tem o primeiro nome



nome = str(input('Qual seu nome? ')).strip()
maiúsculo = nome.upper()
minúsculo = nome.lower()
nomesplit = nome.split()
pnome = len(nomesplit[0])
snome = len(nomesplit[1])
print('Seu nome maiúsculo fica: {}'.format(nome.upper()))
print('Seu nome minúsculo fica: {}'.format(nome.lower()))
print('A quantidade de letras no seu nome, sem espaço é: {}'.format(len(nome) - nome.count(' ')))
print('A quantidade de letras do seu primeiro nome é {}'.format(pnome))
print('A quantidade de letras do seu segundo nome é {}'.format(snome))

