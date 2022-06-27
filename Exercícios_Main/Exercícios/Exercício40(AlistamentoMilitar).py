from datetime import date
anonascimento = int(input('Qual seu ano de nascimento? '))
ano = date.today().year
idade = (ano - anonascimento)
idadefaltante = 18 - idade
anopassado = idade - 18
anodevia = ano - anopassado
anoirá = ano + idadefaltante
if idade <= 18 and idade != 18 :
    print('Ainda não está na hora de se alistar, você poderá se alistar em {} anos\nO ano será: {}'.format(idadefaltante, anoirá))
elif idade == 18:
    print('Você tem {} anos! É hora de alistar!'.format(18))
elif idade >= 18 and idade != 18:
    print('Já passou da hora de alistar! Já se passaram {} anos desde o seu prazo de alistamento!\nVocê devia ter se alistado em {}'.format(anopassado, anodevia))
