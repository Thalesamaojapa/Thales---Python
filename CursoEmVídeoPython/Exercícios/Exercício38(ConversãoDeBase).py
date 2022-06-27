n = int(input('Digite o número a ser convertido: '))
tipo = int(input('Digite 1 para binário, 2 para octal e 3 para hexadecimal: '))
if tipo == 1:
    print('{} convertido pra binário fica:{}'.format(n, bin(n).replace('0b', ' ')))
elif tipo == 2:
    print('{} convertido pra octal fica:{}'.format(n, oct(n).replace('0o', ' ')))
elif tipo == 3:
    print('{} convertido pra hexadecimal fica:{}'.format(n, hex(n).replace('0x', ' ')))
else:
    print('Digite um número entre os propostos! Deixe de ser burro!')
    