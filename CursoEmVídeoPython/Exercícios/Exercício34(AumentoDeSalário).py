#aumentado em 10% se for acima de 1250 e em 15% se for igual ou menor que 1250
salario = float(input('Digite aqui seu salário. R$: '))
salario10 = salario + salario * (10 / 100)
salario15 = salario + salario * (15 / 100 )
if salario == 1250 or salario <= 1250:
    print('Seu novo salário será de R${:.2f}'.format(salario15))
else:
    print('Seu novo salário será de R${:.2f}'.format(salario10))
