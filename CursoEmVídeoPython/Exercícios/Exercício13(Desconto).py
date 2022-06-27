#faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preço = float(input('Qual o preço do produto? R$'))
print('Na liquidação, esse produto com 5% de desconto custaria apenas R${:.2f}'.format(preço - preço * 5 / 100 ))