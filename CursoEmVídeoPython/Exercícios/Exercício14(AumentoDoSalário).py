#crie um programa que leia o salário de um funcionario e diga quanto ele teria com 15% de aumento

salario = float(input('Digite aqui seu salário: '))
aumento = salario + salario * 15 / 100
print('Com aumento de 15% você passaria a ganhar: {:.2f}'.format(aumento))
