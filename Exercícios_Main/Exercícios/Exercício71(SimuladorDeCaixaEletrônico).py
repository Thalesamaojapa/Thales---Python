print('=-' * 20)
print('Bem-Vindo ao Banco Thales!')
print('=-' * 20)
valor = int(input('Digite o valor que deseja sacar. R$: '))
céd = 50
total = valor
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'O total de cédulas de R${céd} a serem retiradas é {totcéd}')
        totcéd = 0
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        elif total == 0:
            break
        