tabela = ('fortaleza', 'athletico-PR', 'Atlético MG', 'Bragantino', 'Palmeiras',
'Bahia', 'Flamengo', 'Atlético-GO', 'Fluminense', 'Santos', 'Corinthians', 'Ceará', 'Internacional', 'Cuiabá',
'São Paulo', 'Chapecoense', 'Juventude', 'Sport Recife', 'América-MG', 'Grêmio')
print('=-' * 72)
print(tabela)
print('=-' * 72)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('=-' * 72)
print(f'Os 4 ultimos colocados são: {tabela[-4:]}')
print('=-' * 72)
print(f'Os times em ordem alfabética: {sorted(tabela)}')
print('=-' * 72)
print(f'O Internacional está na posição: {tabela.index("Internacional") + 1}º')
