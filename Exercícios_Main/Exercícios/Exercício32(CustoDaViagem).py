km = float(input('Quantos Km tem a viagem? '))
preço1 = km * 0.50
preço2 = km * 0.45
if km <= 200:
    print('Sua viagem custará: R${:.2f}'.format(preço1))
else:
    print('Sua viagem custará: R${:.2f}'.format(preço2))
