    
time = list()
infos = dict()
gols = list()
while True:
    infos.clear()
    infos['Nome'] = input('Nome do jogador: ').capitalize()
    num = int(input(f'Quantas partidas {infos["Nome"]} jogou? '))
    gols.clear()
    for c in range(0, num):
        gols.append(int(input(f'Quantos gols {infos["Nome"]} fez na partida {c + 1}? ')))
    infos['Gols'] = gols[:]
    infos['Soma'] = sum(gols)
    time.append(infos.copy())
    print('-' * 30)
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    print('-' * 30)
    if continuar == 'N':
        break
print('=-' * 15)
print('cod ', end='')
for i in infos.keys():
    print(f'{i:<15}', end='')
print()
for cont, item in enumerate(time):
    print(f'{cont:>4} ', end='')
    for d in item.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 20)
while True:
    escolha = int(input('Digite o código de um jogador para mostrar seus dados! (999 para): '))
    if escolha == 999:
        break
    elif escolha >= len(time):
        print('Código inválido. Tente novamente')
    else:
        print(f'-- Levantamento do jogador {time[escolha]["Nome"]}')
        for cont, gol in enumerate(time[escolha]["Gols"]):
            print(f'Na partida {cont + 1}, fez {gol} gols')