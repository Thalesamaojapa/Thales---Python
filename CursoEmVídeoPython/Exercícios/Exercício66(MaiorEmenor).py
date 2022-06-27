continuar = 'S'
num = int(input('Digite um número: '))
soma = num
cont = 1
continuar = input('Quer contunar? [S/N] ').strip().upper()[0]
maior = menor = num
while continuar == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    continuar = input('Quer continar? [S/N] ').strip().upper()[0]
if cont == 1:
    print('Você digitou apenas 1 número...Tente digitar mais!')
else:
    print(f'Você digitou {cont} números e a média entre eles é {soma / cont}')
    print(f'O maior valor foi {maior} e o menor {menor}')
        
    

