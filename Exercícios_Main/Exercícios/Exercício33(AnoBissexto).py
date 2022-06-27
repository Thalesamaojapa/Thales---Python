from datetime import date
ano = int(input('Digite o ano a ser analizado. Digite 0 para analizar o ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('Sim! {} é um ano bissexto'.format(ano))
else:
    print('Não! {} não é um ano bissexto'.format(ano))
    