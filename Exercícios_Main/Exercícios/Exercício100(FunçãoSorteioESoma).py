from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 númeoros da lista: ',end='')
    for c in range(0,5):
        lista.append(randint(0, 50))
        sleep(0.5)
        print(lista[c], end=' ', flush=True)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}!')

números = list()

sorteia(números)
somaPar(números)


