import random

número = int(input('Escolha um número entre 1 e 5! '))
númerosorteado = random.randint(1, 5)
if número == númerosorteado:
    print('Parabéns! Você ganhou!')
else:
    print('Não foi desta vez! Tente novamente! Obs: pensei em {} '.format(númerosorteado))

