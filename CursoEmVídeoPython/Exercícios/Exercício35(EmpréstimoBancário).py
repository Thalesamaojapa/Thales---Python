print('Olá! Para aprovrar seu empréstimo, precisarei de algumas informações básicas!')
casa = float(input('Qual o valor da casa? R$: '))
sala = float(input('Qual o seu salário mensal? R$:'))
anos = float(input('Em quantos anos você pretende pagar o empréstimo? Anos: '))
mes = anos * 12
prestacao = casa / mes
if prestacao >= sala * (30 / 100): 
    print('Seu empréstimo foi \033[1;31mNEGADO\033[m!')
else:
    print('Seu empéstimo foi \033[1;32mAPROVADO\030[m! Sua prestação mensal será de R${:.2f}'.format(prestacao))
