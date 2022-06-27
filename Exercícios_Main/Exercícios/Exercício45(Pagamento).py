preço = float(input('Qual o valor do produto? R$: '))
preçojuros = preço + preço * (20 / 100)
print('Digite 1 para pagamento à vista em dinheiro ou cheque!')
print('Digite 2 para pagamento à vista no cartão!')
print('Digite 3 para pagamento em até 2x no cartão')
print('Digite 4 para pagamento em 3x ou mais no cartão')
cond = int(input('Escolha um método de pagamento: '))
if cond == 3 or cond == 4:
    parcelas = int(input('Em quantas parcelas você gostaria de fazer? '))
if 5 <= cond:
    print('O programa aceita apenas números entre 1 e 4! Selecione um método de pagamento válido! ')
elif cond == 1:
    print('Utilizando essa forma de pagamento você ganha 10% de desconto! O novo preço será de: R${:.2f}'.format(preço - preço * (10 / 100)))
elif cond == 2:
    print('Utilizando essa forma de pagamento você ganha 5% de desconto! O novo preço será de: R${:.2f}'.format(preço - preço * (5 / 100)))
elif cond == 3:
    print('Utilizando essa forma de pagamento você não tem nenhum desconto! O preço continuará sendo de: R${:.2f}\nSerão cobradas {} parcelas de R${:.2f} cada'.format(preço, parcelas, preço / parcelas))
elif cond == 4:
    print('Utilizando essa forma de pagamento você terá 20% de juros! O novo preço será:R${:.2f}\nSerão cobradas {} parcelas de R${:.2f} cada'.format(preçojuros, parcelas, preçojuros / parcelas))

