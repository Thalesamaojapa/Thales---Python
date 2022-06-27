num = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: '))
, int(input('Digite o terceiro número: ')), int(input('Digite o último número: ')))
cont = 0
for n in num:
    if n == 9:
        cont += 1
print(f'O número 9 aparece: {cont} vezes')
if 3 in num:
    print(f'O número 3 está na posição: {num.index(3) + 1}')
print('Os números pares são:', end='')
for n in num:
    if n % 2 == 0:
        print(end=' 'f'{n},')    
        