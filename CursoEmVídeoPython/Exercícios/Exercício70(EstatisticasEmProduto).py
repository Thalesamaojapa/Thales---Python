from typing import overload


soma = tot = barato = 0
nomem = ''
print('=-' * 20)
print('Lojinha do Main Quinn')
print('=-' * 20)
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto. R$: '))
    soma += preco
    if preco > 1000:
        tot += 1
    if nomem == '' and barato == 0:
        nomem = nome
        barato = preco
    if preco < barato:
        barato = preco
        nomem = nome
    print('=-' * 20)
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    print('=-' * 20)
    if continuar == 'N':
        break
print(f'O total das compras foi: R${soma:.2f}')
print(f'O total de produtos que custam mais de R$1000 é: {tot}')
print(f'O produto mais barato foi {nomem} que custa R${barato:.2f}')
        

