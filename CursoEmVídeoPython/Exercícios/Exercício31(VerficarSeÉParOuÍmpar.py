número = str(input('Digite um número: '))

if número[-1] == '1' or número[-1] == '3' or número[-1] == '5' or número[-1] == '7' or número[-1] == '9':
    print('Seu número, {}, é ímpar!'.format(número))
else:
    print('Seu número, {}, é par!'.format(número))
