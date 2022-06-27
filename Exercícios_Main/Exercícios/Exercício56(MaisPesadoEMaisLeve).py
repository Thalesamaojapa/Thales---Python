maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite aqui o peso da {} pessoa: Kg: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso é {}Kg e o maior {}Kg'.format(menor, maior))
