import moeda

preço = float(input('Digite o preço. R$: '))
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'Aumentando {preço} em 10% temos {moeda.pct(preço, 10)}')