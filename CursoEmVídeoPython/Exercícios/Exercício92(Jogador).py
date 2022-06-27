infos = dict()
gols = list()
soma = 0
infos['Nome'] = input('Nome do jogador: ')
num = int(input(f'Quantas partidas {infos["Nome"]} jogou? '))
for c in range(0, num):
    gols.append(int(input(f'Quantos gols {infos["Nome"]} fez na partida {c + 1}? ')))
infos['Gols'] = gols[:]
infos['Soma'] = sum(gols)
print(infos)
print('=-' * 15)
for k, v in infos.items():
    print(f'{k} tem o valor: {v}')
print('=-' * 15)
print(f'O jogador {infos["Nome"]} jogou {num} partidas')
for cont, gol in enumerate(gols):
        print(f'    => Na partida {cont + 1}, fez {gol} gols. ')
print(f'Foi um total de {infos["Soma"]} gols')