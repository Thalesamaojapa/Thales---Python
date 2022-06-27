lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'A lista tem {len(lista)} elementros')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente: {lista}')
if 5 in lista:
    print('Encontrei o número 5 na lista!')
else:
    print('Não encontrei o número 5 na lista :(')