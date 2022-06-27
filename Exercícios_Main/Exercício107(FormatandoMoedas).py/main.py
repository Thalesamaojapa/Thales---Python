import formatação

preço = float(input('Digite o preço. R$: '))
print(f'O dobro de {formatação.formatar(preço)} é {formatação.dobro(preço)}')
print(f'A metade de {formatação.formatar(preço)} é {formatação.metade(preço)}')
print(f'Aumentando {formatação.formatar(preço)} em 10% temos {formatação.pct(preço, 10)}')