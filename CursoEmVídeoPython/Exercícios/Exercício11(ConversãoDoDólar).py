#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considerando 1dólar = 3,27reais

real = float(input('Quanto reais você tem? R$'))
dolar = (real / 3.27)
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))

