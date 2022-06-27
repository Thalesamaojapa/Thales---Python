cont = 0
tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
        cont = cont + 1   
    else:
        print('\033[31m', end=' ')
    print(c, end=' ') 
print('\n\033[mEsse número foi dividido {} vezes'.format(cont), end=' ')  
if tot == 2:
    print('e por isso é primo')
else:   
    print('e por isso não é primo!')
 