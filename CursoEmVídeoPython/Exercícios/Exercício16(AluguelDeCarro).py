#escreva um programa que pergunte a quantidade de km percorrido por um carro alugado e a quantidade
#de dias que ele foi alugado. calcule o preço a pagar. 1 dia = 60reais , 1km rodado = 0.15reais

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados? Km: '))
custo = (dias * 60) + (km * 0.15) 
print('O valor a pagar pelo aluguel do carro será: R${:.2f}'.format(custo))
