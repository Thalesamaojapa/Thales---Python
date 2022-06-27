lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
       lista.append(num)
       print('Número adicionado com sucesso!')
    elif num in lista:
       print('Número duplicado... não adicionarei na lista!')
    continuar = input('Deseja adcionar outro valor? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
       break
print(f'Você digitou os valores: {lista}')
lista.sort()
print(f'Ordenados: {lista}')
