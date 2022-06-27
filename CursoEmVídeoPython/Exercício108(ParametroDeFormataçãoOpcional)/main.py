import novo

preço = float(input('Digite o preço. R$: '))
print(f'O dobro de {novo.formatar(preço)} é {novo.dobro(preço, True)}')
print(f'A metade de {novo.formatar(preço)} é {novo.metade(preço)}')
print(f'Aumentando {novo.formatar(preço)} em 10% temos {novo.pct(preço, 10, True)}')