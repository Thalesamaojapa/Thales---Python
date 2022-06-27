from datetime import date
ano = date.today().year
nascimento = int(input('Digite aqui seu ano de nascimento: '))
idade = ano - nascimento
if idade == 9 or idade <= 9:
    print('Segundo a Confederação Nacional De Natação, você se encaixa na categoria Mirim.')
elif idade == 14 or idade >= 9 and idade <= 14 and idade:
    print('Segundo a Confederação Nacional De Natação, você se encaixa na categoria Infatil.')
elif idade == 19 or idade >= 14 and idade <= 19 and idade:
    print('Segundo a Confederação Nacional De Natação, você se encaixa na categoria Junior.')
elif idade == 20:
    print('Segundo a Confederação Nacional De Natação, você se encaixa na categoria Sênior.')
elif idade >= 20:
    print('Segundo a Confederação Nacional De Natação, você se encaixa na categoria Master.')    
    