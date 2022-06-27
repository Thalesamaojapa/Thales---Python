from random import randint
from operator import itemgetter
jogo = {'Jogador1': randint(0, 6),
        'Jogador2': randint(0, 6),
        'Jogador3': randint(0, 6),
        'Jogador4': randint(0, 6)}
print(jogo)
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1} lugar: {v[0]} com {v[1]}')
