valores = []
maior = menor = 0
for c in range(0,5):
    valores.append(int(input(f'Digite o {c + 1}º valor: ')))
    if c == 0:
        maior = menor = valores[0]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('Você digitou os valores: ')
for v in valores:
    print(f'{v}', end=' / ')
print(f'\nO menor valor é {menor}.', end=' ')
print('Encontrei ele nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(i + 1, end=', ')
print(f'\nO maior valor é {maior}.', end=' ')
print('Encontrei ele nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(i + 1, end=', ')