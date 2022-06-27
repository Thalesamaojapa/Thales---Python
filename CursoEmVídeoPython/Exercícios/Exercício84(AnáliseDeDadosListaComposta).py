info = []
tot = menor = maior = 0
pessoas = []
while True:
    info.append(input('Nome: '))
    info.append(float(input('Peso. Kg: ')))
    pessoas.append(info[:])
    info.clear()
    continuar = input('Deseja cadastrar outra pessoa? [S/N]: ').strip().upper()[0]
    tot += 1
    if continuar == 'N':
        break
for c, dados in enumerate(pessoas):
    if c == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
print(f'O total de pessoas que foram cadastradas é de {tot}')
print(f'O maior peso é {maior}Kg, a(s) pessoa(s) que tem(ê) esse peso é/são:',end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso é {menor}Kg, a(s) pessoa(s) que tem(ê) esse peso é/são:',end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')





    